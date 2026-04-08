"""
Equation dataclass for thermal property regression equations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Equation:
    """
    A single multivariate linear regression equation for predicting
    thermal conductivity (TC), thermal diffusivity (TD), or specific
    heat capacity (SHC) from well-log inputs.

    Parameters
    ----------
    id : str
        Equation identifier (e.g. ``"A12"``, ``"B5"``, ``"C30"``).
    property : str
        Target property: ``"tc"``, ``"td"``, or ``"shc"``.
    rock_group : str
        Sedimentary rock group: ``"clastic"``, ``"carbonate"``, or
        ``"evaporite"``.
    required_inputs : tuple of str
        Names of the well-log inputs this equation requires
        (subset of ``"rho_b"``, ``"phi_n"``, ``"U"``, ``"dt"``, ``"vsh"``).
    intercept : float
        Regression intercept (B0).
    coefficients : mapping of str to float
        Regression coefficients keyed by input name.
    reference : str
        Bibliographic reference for this equation.
    """

    id: str
    property: str
    rock_group: str
    required_inputs: tuple[str, ...]
    intercept: float
    coefficients: Mapping[str, float]
    reference: str
    rms: float = 0.0

    def predict(self, **kwargs: float) -> float:
        """
        Evaluate the regression equation for the given input values.

        Parameters
        ----------
        **kwargs : float
            Well-log values keyed by input name. All names listed in
            :attr:`required_inputs` must be present.

        Returns
        -------
        float
            Predicted thermal property value.

        Raises
        ------
        ValueError
            If any required input is missing from *kwargs*.

        """
        missing = [k for k in self.required_inputs if k not in kwargs]
        if missing:
            raise ValueError(
                f"Equation {self.id} is missing required inputs: {missing}"
            )

        value = self.intercept
        for k in self.required_inputs:
            value += self.coefficients.get(k, 0.0) * kwargs[k]
        return value