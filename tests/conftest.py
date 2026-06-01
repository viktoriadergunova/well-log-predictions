"""
Shared pytest fixtures for  test suite.
"""
import numpy as np
import pandas as pd
import pytest


ROCK_GROUPS = ["clastic", "carbonate", "evaporite"]
PROPS = ["tc", "td", "shc"]


@pytest.fixture
def minimal_clastic_df():
    """Smallest valid DataFrame: one clastic row with RHOB only."""
    return pd.DataFrame({
        "DEPTH":      [100.0],
        "ROCK_GROUP": ["clastic"],
        "RHOB":       [2.3],
    })


@pytest.fixture
def full_clastic_df():
    """Clastic rows covering all five log columns + a NaN row."""
    return pd.DataFrame({
        "DEPTH":      [100.0, 200.0, 300.0, 400.0],
        "ROCK_GROUP": ["clastic"] * 4,
        "RHOB":       [2.3,    2.5,    2.1,    np.nan],
        "PHIN":       [0.1,    0.15,   np.nan, np.nan],
        "U":          [3.5,    np.nan, np.nan, np.nan],
        "DT":         [70.0,   np.nan, np.nan, np.nan],
        "VSH":        [0.2,    0.3,    np.nan, np.nan],
    })


@pytest.fixture
def mixed_rock_group_df():
    """DataFrame with all three rock groups."""
    return pd.DataFrame({
        "DEPTH":      [100.0, 200.0, 300.0],
        "ROCK_GROUP": ["clastic", "carbonate", "evaporite"],
        "RHOB":       [2.3,   2.7,   2.1],
        "PHIN":       [0.1,   0.05,  0.2],
    })