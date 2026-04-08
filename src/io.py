"""
Input/output utilities for the wellog package.

The main entry point is :func:`load_dataframe`, which accepts a
pandas DataFrame containing well-log data and returns a validated,
standardised copy ready for preprocessing and prediction.
"""

from __future__ import annotations

import pandas as pd

from .utils import normalize_rock_group


# All well-log columns the library understands.
KNOWN_LOG_COLUMNS = {"RHOB", "PHIN", "U", "DT", "VSH"}

# Required non-log columns.
DEPTH_COLUMN = "DEPTH"
ROCK_GROUP_COLUMN = "ROCK_GROUP"

# All columns the library understands.
KNOWN_COLUMNS = KNOWN_LOG_COLUMNS | {DEPTH_COLUMN, ROCK_GROUP_COLUMN}


def load_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate and standardise a well-log DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame. Column names are matched case-insensitively.
        Must contain:

        * ``DEPTH`` -- measured depth column.
        * ``ROCK_GROUP`` -- one of ``"clastic"``, ``"carbonate"``, or
          ``"evaporite"`` per row. Integers ``-3``, ``-2``, ``-1`` are
          also accepted.
        * At least one of: ``RHOB``, ``PHIN``, ``U``, ``DT``, ``VSH``.

    Returns
    -------
    pd.DataFrame
        A copy of *df* with:

        * column names uppercased,
        * a validated ``ROCK_GROUP`` column containing normalised
          strings (``"clastic"``, ``"carbonate"``, or ``"evaporite"``).

    Raises
    ------
    TypeError
        If *df* is not a :class:`pandas.DataFrame`.
    ValueError
        If ``DEPTH`` is missing, no recognised log columns are found,
        or ``ROCK_GROUP`` is missing or contains invalid values.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            f"Expected a pandas DataFrame, got {type(df).__name__!r}."
        )

    df = df.copy()

    # --- normalise column names -----------------------------------------
    df.columns = [c.strip().upper() for c in df.columns]

    # --- check DEPTH is present -----------------------------------------
    if DEPTH_COLUMN not in df.columns:
        raise ValueError(
            "No 'DEPTH' column found. The DataFrame must contain a depth column."
        )

    # --- check at least one known log column is present -----------------
    present = KNOWN_LOG_COLUMNS & set(df.columns)
    if not present:
        raise ValueError(
            f"DataFrame contains none of the recognised log columns "
            f"({sorted(KNOWN_LOG_COLUMNS)}). "
            f"Found: {sorted(df.columns)}."
        )

    # --- resolve rock_group ---------------------------------------------
    if ROCK_GROUP_COLUMN not in df.columns:
        raise ValueError(
            "No 'ROCK_GROUP' column found in the DataFrame."
        )

    try:
        df[ROCK_GROUP_COLUMN] = df[ROCK_GROUP_COLUMN].apply(
            normalize_rock_group
        )
    except (ValueError, KeyError) as exc:
        raise ValueError(
            f"Invalid value in 'ROCK_GROUP' column: {exc}"
        ) from exc

    return df