"""
Prediction utilities for the wellog package.

The two main entry points are:

* :func:`predict` — dispatcher, choose mode ``"best_fit"`` or
  ``"available_logs"``.
* :func:`predict_best_fit` — for each row, pick the equation with the
  lowest RMS among those whose required inputs are all present and whose
  rock group matches the row.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .equation import Equation
from .equation_data import EQUATIONS
from .io import KNOWN_LOG_COLUMNS, ROCK_GROUP_COLUMN


def _equations_for(rock_group: str, prop: str) -> list[Equation]:
    """Return all equations matching rock group and property."""
    return [
        eq for eq in EQUATIONS.values()
        if eq.rock_group == rock_group and eq.property == prop
    ]


def _best_equation(equations: list[Equation]) -> Equation | None:
    """
    Pick the equation with the lowest RMS
    """
    if not equations:
        return None
    # take lowest rms
    return min(equations, key=lambda eq: (eq.rms, -len(eq.required_inputs)))

def predict_best_fit(df: pd.DataFrame, prop: str) -> pd.DataFrame:
    """
        For each row pick the best applicable equation and return predicted
    values and the equation used per row.

    Parameters
    ----------
    df : pd.DataFrame
        Validated DataFrame from :func:`wellog.io.load_dataframe`.
    prop : str
        Target thermal property: ``"tc"``, ``"td"``, or ``"shc"``.

    Returns
    -------
    pd.DataFrame
        Two columns: ``"<prop>_best_fit"`` (predicted value) and
        ``"<prop>_best_fit_eq"`` (equation id used). Rows where no
        applicable equation exists have ``NaN`` and ``None``.
    """
    values = np.full(len(df), np.nan)
    equations_used = np.full(len(df), None, dtype=object)

    for rg, rg_df in df.groupby(ROCK_GROUP_COLUMN):
        all_candidates = _equations_for(rg, prop)
        if not all_candidates:
            continue

        relevant_cols = list(set().union(*(eq.required_inputs for eq in all_candidates)))
        available_cols = [c for c in relevant_cols if c in rg_df.columns]
        
        for _, subset in rg_df.groupby([rg_df[c].notna() for c in available_cols]):
            if subset.empty:
                continue
                
            first_row = subset.iloc[0]
            present_logs = {col for col in available_cols if pd.notna(first_row[col])}
            
            viable = [
                eq for eq in all_candidates 
                if all(req in present_logs for req in eq.required_inputs)
            ]
            
            best_eq = _best_equation(viable)
            if best_eq:
                equations_used[subset.index] = best_eq.id
                input_kwargs = {col: subset[col] for col in best_eq.required_inputs}
                values[subset.index] = best_eq.predict(**input_kwargs)

    main_res = pd.DataFrame({
        f"{prop}_pred": pd.array(values, dtype="float64"),
        f"{prop}_eq": equations_used,
    }, index=df.index)


    from .uncertainty import calculate_eq_spread
    uncertainty_res = calculate_eq_spread(
        df, 
        prop, 
        main_res[f"{prop}_pred"], 
        main_res[f"{prop}_eq"]
    )

    return pd.concat([main_res, uncertainty_res], axis=1)

def predict_available_logs(df: pd.DataFrame, prop: str) -> pd.DataFrame:
    values = np.full(len(df), np.nan)
    equations_used = np.full(len(df), None, dtype=object)

    available_in_headers = [c for c in KNOWN_LOG_COLUMNS if c in df.columns]

    for rg, rg_df in df.groupby(ROCK_GROUP_COLUMN):
        all_candidates = _equations_for(rg, prop)
        
        for _, subset in rg_df.groupby([rg_df[c].notna() for c in available_in_headers]):
            if subset.empty:
                continue
                
            first_row = subset.iloc[0]
            present_in_row = frozenset(
                col for col in available_in_headers if pd.notna(first_row[col])
            )
            

            match = next(
                (
                    eq for eq in all_candidates 
                    if frozenset(eq.required_inputs) == present_in_row
                ),
                None,
            )
            
            if match:
                equations_used[subset.index] = match.id
                input_kwargs = {col: subset[col] for col in match.required_inputs}
                values[subset.index] = match.predict(**input_kwargs)
            else:
                header_logs = frozenset(available_in_headers)
                header_match = next(
                    (eq for eq in all_candidates if frozenset(eq.required_inputs) == header_logs),
                    None
                )
                if header_match:
                    equations_used[subset.index] = header_match.id

    main_res = pd.DataFrame({
        f"{prop}_pred": pd.array(values, dtype="float64"),
        f"{prop}_eq": equations_used,
    }, index=df.index)


    from .uncertainty import calculate_uncertainty
    uncertainty_res = calculate_uncertainty(
        df, 
        prop, 
        main_res[f"{prop}_pred"], 
        main_res[f"{prop}_eq"]
    )

    return pd.concat([main_res, uncertainty_res], axis=1)

def predict(
    df: pd.DataFrame,
    prop: str,
    mode: str = "best_fit",
) -> pd.DataFrame:
    _MODES = {
        "best_fit": predict_best_fit,
        "available_logs": predict_available_logs,
    }
    if mode not in _MODES:
        raise ValueError(
            f"Unknown mode {mode!r}. Choose 'best_fit' or 'available_logs'."
        )

    fn = _MODES[mode]

    if prop == "all":
        return pd.concat([fn(df, p) for p in ("tc", "td", "shc")], axis=1)

    return fn(df, prop)