from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Equation:
    id: str
    property: str
    rock_group: str
    required_inputs: tuple[str, ...]
    intercept: float
    coefficients: Mapping[str, float]
    reference: str

    def predict(self, **kwargs: float) -> float:
        missing = [k for k in self.required_inputs if k not in kwargs]
        if missing:
            raise ValueError(f"{self.id} missing inputs: {missing}")

        value = self.intercept
        for k in self.required_inputs:
            value += self.coefficients.get(k, 0.0) * kwargs[k]
        return value