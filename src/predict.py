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

from typing import Iterator

import numpy as np
import pandas as pd

from .equation import Equation
from .equation_data import EQUATIONS
from .io import KNOWN_LOG_COLUMNS, ROCK_GROUP_COLUMN


def _iter_row_inputs(
    df: pd.DataFrame,
    equation: Equation,
) -> Iterator[dict[str, float] | None]:
    """
    Per-row input dicts for a single equation.

    ``None`` for rows where any required input is missing or NaN.
    """
    required = equation.required_inputs

    missing_cols = [col for col in required if col not in df.columns]
    if missing_cols:
        for _ in range(len(df)):
            yield None
        return

    subset = df[list(required)]
    for _, row in subset.iterrows():
        if row.isna().any():
            yield None
        else:
            yield {col: float(row[col]) for col in required}


def _equations_for(rock_group: str, prop: str) -> list[Equation]:
    """Return all equations matching rock group and property."""
    return [
        eq for eq in EQUATIONS.values()
        if eq.rock_group == rock_group and eq.property == prop
    ]


def _applicable_equations(
    df: pd.DataFrame,
    rock_group: str,
    prop: str,
) -> list[Equation]:
    """
    Return equations for *rock_group* and *prop* whose required inputs
    are all present as columns in *df*.
    """
    available_cols = set(df.columns)
    return [
        eq for eq in _equations_for(rock_group, prop)
        if all(col in available_cols for col in eq.required_inputs)
    ]


def _best_equation(equations: list[Equation]) -> Equation | None:
    """
    Pick the equation with the lowest RMS
    """
    if not equations:
        return None
    return min(equations, key=lambda eq: (eq.rms, -len(eq.required_inputs)))


def predict_best_fit(
    df: pd.DataFrame,
    prop: str,
) -> pd.DataFrame:
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

    rock_groups = df[ROCK_GROUP_COLUMN]

    for rg in rock_groups.unique():
        equations = _applicable_equations(df, rg, prop)
        if not equations:
            continue

        row_indices = np.where(rock_groups == rg)[0]
        sub_df = df.iloc[row_indices]

        # Pre-compute per-row inputs for every candidate equation
        eq_inputs: dict[str, list[dict | None]] = {
            eq.id: list(_iter_row_inputs(sub_df, eq)) for eq in equations
        }

        for local_i, global_i in enumerate(row_indices):
            candidates = [
                eq for eq in equations
                if eq_inputs[eq.id][local_i] is not None
            ]
            best = _best_equation(candidates)
            if best is None:
                continue
            values[global_i] = best.predict(**eq_inputs[best.id][local_i])
            equations_used[global_i] = best.id

    return pd.DataFrame(
        {
            f"{prop}_best_fit": pd.array(values, dtype="float64"),
            f"{prop}_best_fit_eq": equations_used,
        },
        index=df.index,
    )

def predict_available_logs(
    df: pd.DataFrame,
    prop: str,
) -> pd.DataFrame:
    
    values = np.full(len(df), np.nan)
    equations_used = np.full(len(df), None, dtype=object)
 
    rock_groups = df[ROCK_GROUP_COLUMN]
    # Identify which logs are present in the dataframe columns
    available_cols = set(df.columns)
    available_logs = frozenset(KNOWN_LOG_COLUMNS & available_cols)
 
    for rg in rock_groups.unique():
        # Find the equation that matches the column headers exactly
        match = next(
            (
                eq for eq in _equations_for(rg, prop)
                if frozenset(eq.required_inputs) == available_logs
            ),
            None,
        )

        if match is None:
            continue
 
        row_indices = np.where(rock_groups == rg)[0]
        sub_df = df.iloc[row_indices]
 
        # Iterate through the rows for this rock group
        for local_i, global_i in enumerate(row_indices):
            # We always record the equation ID because it matches the available columns
            equations_used[global_i] = match.id

            # Get inputs for this specific row
            inputs = next(
                inp for j, inp in enumerate(_iter_row_inputs(sub_df, match))
                if j == local_i
            )
            
            # Only calculate value if there are no NaNs in the row
            if inputs is not None:
                values[global_i] = match.predict(**inputs)
 
    return pd.DataFrame(
        {
            f"{prop}_available_logs": pd.array(values, dtype="float64"),
            f"{prop}_available_logs_eq": equations_used,
        },
        index=df.index,
    )
 
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