from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, List


# -------------------------
# Equation class
# -------------------------
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


# -------------------------
# Equation
# -------------------------
EQUATIONS: dict[str, Equation] = {
    "A1": Equation(
        id="A1",
        property="tc",
        rock_group="clastic",
        required_inputs=("rho_b",),
        intercept=5.310281851695268,
        coefficients={"rho_b": -0.809},
        reference="Fuchs et al. (2015), Table 3, A1",
    ),

    "A2": Equation(
        id="A2",
        property="tc",
        rock_group="clastic",
        required_inputs=("phi_n",),
        intercept=5.336946806325883,
        coefficients={"phi_n": -8.14},
        reference="Fuchs et al. (2015), Table 3, A2",
    ),

    "A3": Equation(
        id="A3",
        property="tc",
        rock_group="clastic",
        required_inputs=("U",),
        intercept=-0.9286487673553432,
        coefficients={"U": 0.437},
        reference="Fuchs et al. (2015), Table 3, A3",
    ),

    "A4": Equation(
        id="A4",
        property="tc",
        rock_group="clastic",
        required_inputs=("dt",),
        intercept=3.727633402545825,
        coefficients={"dt": -0.00117},
        reference="Fuchs et al. (2015), Table 3, A4",
    ),

    "A5": Equation(
        id="A5",
        property="tc",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n"),
        intercept=10.730470899024056,
        coefficients={"rho_b": -2.223, "phi_n": -9.21},
        reference="Fuchs et al. (2015), Table 3, A5",
    ),

    "A6": Equation(
        id="A6",
        property="tc",
        rock_group="clastic",
        required_inputs=("rho_b", "U"),
        intercept=2.0898661311489315,
        coefficients={"rho_b": -1.504, "U": 0.483},
        reference="Fuchs et al. (2015), Table 3, A6",
    ),

    "A7": Equation(
        id="A7",
        property="tc",
        rock_group="clastic",
        required_inputs=("rho_b", "dt"),
        intercept=15.692279441332015,
        coefficients={"rho_b": -3.455, "dt": -0.01725},
        reference="Fuchs et al. (2015), Table 3, A7",
    ),

    "A8": Equation(
        id="A8",
        property="tc",
        rock_group="clastic",
        required_inputs=("phi_n", "U"),
        intercept=5.340386968587341,
        coefficients={"phi_n": -8.14, "U": 0.0},
        reference="Fuchs et al. (2015), Table 3, A8",
    ),

    "A9": Equation(
        id="A9",
        property="tc",
        rock_group="clastic",
        required_inputs=("phi_n", "dt"),
        intercept=3.4644130452290303,
        coefficients={"phi_n": -9.07, "dt": 0.00847},
        reference="Fuchs et al. (2015), Table 3, A9",
    ),

    "A10": Equation(
        id="A10",
        property="tc",
        rock_group="clastic",
        required_inputs=("U", "dt"),
        intercept=-2.2454333360241066,
        coefficients={"U": 0.469, "dt": 0.00405},
        reference="Fuchs et al. (2015), Table 3, A10",
    ),

    "A11": Equation(
        id="A11",
        property="tc",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=10.522454531025481,
        coefficients={"rho_b": -2.227, "phi_n": -9.07, "U": 0.019},
        reference="Fuchs et al. (2015), Table 3, A11",
    ),

    "A12": Equation(
        id="A12",
        property="tc",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=14.400212247441985,
        coefficients={"rho_b": -3.157, "phi_n": -8.97, "dt": -0.00634},
        reference="Fuchs et al. (2015), Table 3, A12",
    ),

    "A13": Equation(
        id="A13",
        property="tc",
        rock_group="clastic",
        required_inputs=("rho_b", "U", "dt"),
        intercept=8.49835154940508,
        coefficients={"rho_b": -3.032, "U": 0.45, "dt": -0.01028},
        reference="Fuchs et al. (2015), Table 3, A13",
    ),

    "A14": Equation(
        id="A14",
        property="tc",
        rock_group="clastic",
        required_inputs=("phi_n", "U", "dt"),
        intercept=3.107614839366339,
        coefficients={"phi_n": -8.86, "U": 0.028, "dt": 0.00855},
        reference="Fuchs et al. (2015), Table 3, A14",
    ),

    "A15": Equation(
        id="A15",
        property="tc",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=14.324114786675658,
        coefficients={"rho_b": -3.153, "phi_n": -8.93, "U": 0.005, "dt": -0.00631},
        reference="Fuchs et al. (2015), Table 3, A15",
    ),

    "A16": Equation(
        id="A16",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b",),
        intercept=-4.451,
        coefficients={"rho_b": 2.985},
        reference="Fuchs et al. (2015), Table 3, A16",
    ),

    "A17": Equation(
        id="A17",
        property="tc",
        rock_group="carbonate",
        required_inputs=("phi_n",),
        intercept=3.918,
        coefficients={"phi_n": -5.11},
        reference="Fuchs et al. (2015), Table 3, A17",
    ),

    "A18": Equation(
        id="A18",
        property="tc",
        rock_group="carbonate",
        required_inputs=("U",),
        intercept=1.76,
        coefficients={"U": 0.118},
        reference="Fuchs et al. (2015), Table 3, A18",
    ),

    "A19": Equation(
        id="A19",
        property="tc",
        rock_group="carbonate",
        required_inputs=("dt",),
        intercept=5.562,
        coefficients={"dt": -0.012},
        reference="Fuchs et al. (2015), Table 3, A19",
    ),

    "A20": Equation(
        id="A20",
        property="tc",
        rock_group="carbonate",
        required_inputs=("vsh",),
        intercept=3.596,
        coefficients={"vsh": -1.96},
        reference="Fuchs et al. (2015), Table 3, A20",
    ),

    "A21": Equation(
        id="A21",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n"),
        intercept=0.08,
        coefficients={"rho_b": 1.411, "phi_n": -3.15},
        reference="Fuchs et al. (2015), Table 3, A21",
    ),

    "A22": Equation(
        id="A22",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "U"),
        intercept=-6.445,
        coefficients={"rho_b": 4.648, "U": -0.27},
        reference="Fuchs et al. (2015), Table 3, A22",
    ),

    "A23": Equation(
        id="A23",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "dt"),
        intercept=0.237,
        coefficients={"rho_b": 1.632, "dt": -0.006},
        reference="Fuchs et al. (2015), Table 3, A23",
    ),

    "A24": Equation(
        id="A24",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "vsh"),
        intercept=-2.404,
        coefficients={"rho_b": 2.393, "vsh": -1.29},
        reference="Fuchs et al. (2015), Table 3, A24",
    ),

    "A25": Equation(
        id="A25",
        property="tc",
        rock_group="carbonate",
        required_inputs=("phi_n", "U"),
        intercept=4.84179461482062,
        coefficients={"phi_n": -5.88, "U": -0.101},
        reference="Fuchs et al. (2015), Table 3, A25",
    ),

    "A26": Equation(
        id="A26",
        property="tc",
        rock_group="carbonate",
        required_inputs=("phi_n", "dt"),
        intercept=4.426332773014648,
        coefficients={"phi_n": -3.78, "dt": -0.0034},
        reference="Fuchs et al. (2015), Table 3, A26",
    ),

    "A27": Equation(
        id="A27",
        property="tc",
        rock_group="carbonate",
        required_inputs=("phi_n", "vsh"),
        intercept=4.241242964210805,
        coefficients={"phi_n": -4.08, "vsh": -1.17},
        reference="Fuchs et al. (2015), Table 3, A27",
    ),

    "A28": Equation(
        id="A28",
        property="tc",
        rock_group="carbonate",
        required_inputs=("U", "dt"),
        intercept=7.016587102042626,
        coefficients={"U": -0.12, "dt": -0.01418},
        reference="Fuchs et al. (2015), Table 3, A28",
    ),

    "A29": Equation(
        id="A29",
        property="tc",
        rock_group="carbonate",
        required_inputs=("U", "vsh"),
        intercept=3.3916232809303533,
        coefficients={"U": 0.025, "vsh": -1.9},
        reference="Fuchs et al. (2015), Table 3, A29",
    ),

    "A30": Equation(
        id="A30",
        property="tc",
        rock_group="carbonate",
        required_inputs=("dt", "vsh"),
        intercept=5.844915141092354,
        coefficients={"dt": -0.00997, "vsh": -1.48},
        reference="Fuchs et al. (2015), Table 3, A30",
    ),

    "A31": Equation(
        id="A31",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=-2.7956477421996135,
        coefficients={"rho_b": 3.301, "phi_n": -2.43, "U": -0.248},
        reference="Fuchs et al. (2015), Table 3, A31",
    ),

    "A32": Equation(
        id="A32",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=-1.3934489086249424,
        coefficients={"rho_b": 1.763, "phi_n": -4.01, "dt": 0.00344},
        reference="Fuchs et al. (2015), Table 3, A32",
    ),

    "A33": Equation(
        id="A33",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "vsh"),
        intercept=0.5903701058292197,
        coefficients={"rho_b": 1.34, "phi_n": -2.24, "vsh": -1.15},
        reference="Fuchs et al. (2015), Table 3, A33",
    ),

    "A34": Equation(
        id="A34",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "dt"),
        intercept=-4.372579573835685,
        coefficients={"rho_b": 4.005, "U": -0.259, "dt": -0.00253},
        reference="Fuchs et al. (2015), Table 3, A34",
    ),

    "A35": Equation(
        id="A35",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "vsh"),
        intercept=-4.369394853676745,
        coefficients={"rho_b": 4.178, "U": -0.302, "vsh": -1.45},
        reference="Fuchs et al. (2015), Table 3, A35",
    ),

    "A36": Equation(
        id="A36",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "dt", "vsh"),
        intercept=5.009264885870307,
        coefficients={"rho_b": 0.254, "dt": -0.0091, "vsh": -1.45},
        reference="Fuchs et al. (2015), Table 3, A36",
    ),

    "A37": Equation(
        id="A37",
        property="tc",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "dt"),
        intercept=5.8792879138742995,
        coefficients={"phi_n": -3.74, "U": -0.119, "dt": -0.00582},
        reference="Fuchs et al. (2015), Table 3, A37",
    ),

    "A38": Equation(
        id="A38",
        property="tc",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "vsh"),
        intercept=5.464142443949919,
        coefficients={"phi_n": -4.97, "U": -0.13, "vsh": -1.28},
        reference="Fuchs et al. (2015), Table 3, A38",
    ),

    "A39": Equation(
        id="A39",
        property="tc",
        rock_group="carbonate",
        required_inputs=("phi_n", "dt", "vsh"),
        intercept=6.189044842439516,
        coefficients={"phi_n": 1.08, "dt": -0.01226, "vsh": -1.58},
        reference="Fuchs et al. (2015), Table 3, A39",
    ),

    "A40": Equation(
        id="A40",
        property="tc",
        rock_group="carbonate",
        required_inputs=("U", "dt", "vsh"),
        intercept=8.238850476219705,
        coefficients={"U": -0.194, "dt": -0.01345, "vsh": -1.74},
        reference="Fuchs et al. (2015), Table 3, A40",
    ),

    "A41": Equation(
        id="A41",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=-6.192203364923487,
        coefficients={"rho_b": 4.191, "phi_n": -4.25, "U": -0.264, "dt": 0.00749},
        reference="Fuchs et al. (2015), Table 3, A41",
    ),

    "A42": Equation(
        id="A42",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "vsh"),
        intercept=-2.6693541300812935,
        coefficients={"rho_b": 3.534, "phi_n": -1.21, "U": -0.29, "vsh": -1.37},
        reference="Fuchs et al. (2015), Table 3, A42",
    ),

    "A43": Equation(
        id="A43",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "dt", "vsh"),
        intercept=5.772582305742571,
        coefficients={"rho_b": 0.119, "phi_n": 1.0, "dt": -0.01168, "vsh": -1.56},
        reference="Fuchs et al. (2015), Table 3, A43",
    ),

    "A44": Equation(
        id="A44",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "dt", "vsh"),
        intercept=0.33348925413588937,
        coefficients={"rho_b": 2.731, "U": -0.28, "dt": -0.00559, "vsh": -1.54},
        reference="Fuchs et al. (2015), Table 3, A44",
    ),

    "A45": Equation(
        id="A45",
        property="tc",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "dt", "vsh"),
        intercept=9.120545176084255,
        coefficients={"phi_n": 2.36, "U": -0.204, "dt": -0.01863, "vsh": -1.97},
        reference="Fuchs et al. (2015), Table 3, A45",
    ),

    "A46": Equation(
        id="A46",
        property="tc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "dt", "vsh"),
        intercept=1.1537046917854277,
        coefficients={"rho_b": 2.587, "phi_n": 1.08, "U": -0.28, "dt": -0.00838, "vsh": -1.66},
        reference="Fuchs et al. (2015), Table 3, A46",
    ),

    "A47": Equation(
        id="A47",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b",),
        intercept=-3.299012415467577,
        coefficients={"rho_b": 2.361},
        reference="Fuchs et al. (2015), Table 3, A47",
    ),

    "A48": Equation(
        id="A48",
        property="tc",
        rock_group="evaporite",
        required_inputs=("phi_n",),
        intercept=3.40976040613132,
        coefficients={"phi_n": -4.83},
        reference="Fuchs et al. (2015), Table 3, A48",
    ),

    "A49": Equation(
        id="A49",
        property="tc",
        rock_group="evaporite",
        required_inputs=("U",),
        intercept=2.138606210506059,
        coefficients={"U": 0.029},
        reference="Fuchs et al. (2015), Table 3, A49",
    ),

    "A50": Equation(
        id="A50",
        property="tc",
        rock_group="evaporite",
        required_inputs=("dt",),
        intercept=4.807189560581383,
        coefficients={"dt": -0.00974},
        reference="Fuchs et al. (2015), Table 3, A50",
    ),

    "A51": Equation(
        id="A51",
        property="tc",
        rock_group="evaporite",
        required_inputs=("vsh",),
        intercept=3.5990881505073045,
        coefficients={"vsh": -2.31},
        reference="Fuchs et al. (2015), Table 3, A51",
    ),

    "A52": Equation(
        id="A52",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n"),
        intercept=2.5182003375529676,
        coefficients={"rho_b": 0.331, "phi_n": -4.38},
        reference="Fuchs et al. (2015), Table 3, A52",
    ),

    "A53": Equation(
        id="A53",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "U"),
        intercept=-5.703234019806985,
        coefficients={"rho_b": 4.364, "U": -0.335},
        reference="Fuchs et al. (2015), Table 3, A53",
    ),

    "A54": Equation(
        id="A54",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "dt"),
        intercept=1.1376846849202744,
        coefficients={"rho_b": 1.117, "dt": -0.00578},
        reference="Fuchs et al. (2015), Table 3, A54",
    ),

    "A55": Equation(
        id="A55",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "vsh"),
        intercept=-1.2761893073297839,
        coefficients={"rho_b": 1.974, "vsh": -2.02},
        reference="Fuchs et al. (2015), Table 3, A55",
    ),

    "A56": Equation(
        id="A56",
        property="tc",
        rock_group="evaporite",
        required_inputs=("phi_n", "U"),
        intercept=4.029643969917976,
        coefficients={"phi_n": -5.17, "U": -0.077},
        reference="Fuchs et al. (2015), Table 3, A56",
    ),

    "A57": Equation(
        id="A57",
        property="tc",
        rock_group="evaporite",
        required_inputs=("phi_n", "dt"),
        intercept=1.0095567847039892,
        coefficients={"phi_n": -10.87, "dt": 0.01474},
        reference="Fuchs et al. (2015), Table 3, A57",
    ),

    "A58": Equation(
        id="A58",
        property="tc",
        rock_group="evaporite",
        required_inputs=("phi_n", "vsh"),
        intercept=4.170115033419756,
        coefficients={"phi_n": -3.89, "vsh": -1.78},
        reference="Fuchs et al. (2015), Table 3, A58",
    ),

    "A59": Equation(
        id="A59",
        property="tc",
        rock_group="evaporite",
        required_inputs=("U", "dt"),
        intercept=6.198373557710976,
        coefficients={"U": -0.126, "dt": -0.0117},
        reference="Fuchs et al. (2015), Table 3, A59",
    ),

    "A60": Equation(
        id="A60",
        property="tc",
        rock_group="evaporite",
        required_inputs=("U", "vsh"),
        intercept=2.899475774235346,
        coefficients={"U": 0.115, "vsh": -2.52},
        reference="Fuchs et al. (2015), Table 3, A60",
    ),

    "A61": Equation(
        id="A61",
        property="tc",
        rock_group="evaporite",
        required_inputs=("dt", "vsh"),
        intercept=5.586139192189112,
        coefficients={"dt": -0.0084, "vsh": -2.05},
        reference="Fuchs et al. (2015), Table 3, A61",
    ),

    "A62": Equation(
        id="A62",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=-3.8670545040050297,
        coefficients={"rho_b": 3.577, "phi_n": -1.15, "U": -0.293},
        reference="Fuchs et al. (2015), Table 3, A62",
    ),

    "A63": Equation(
        id="A63",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=-6.926475142770707,
        coefficients={"rho_b": 2.226, "phi_n": -12.64, "dt": 0.02662},
        reference="Fuchs et al. (2015), Table 3, A63",
    ),

    "A64": Equation(
        id="A64",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "vsh"),
        intercept=2.5412845977845584,
        coefficients={"rho_b": 0.609, "phi_n": -3.03, "vsh": -1.81},
        reference="Fuchs et al. (2015), Table 3, A64",
    ),

    "A65": Equation(
        id="A65",
        property="tc",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "dt"),
        intercept=0.9439148936432797,
        coefficients={"phi_n": -10.95, "U": 0.003, "dt": 0.01498},
        reference="Fuchs et al. (2015), Table 3, A65",
    ),

    "A66": Equation(
        id="A66",
        property="tc",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "vsh"),
        intercept=4.081480305053707,
        coefficients={"phi_n": -3.82, "U": 0.013, "vsh": -1.81},
        reference="Fuchs et al. (2015), Table 3, A66",
    ),

    "A67": Equation(
        id="A67",
        property="tc",
        rock_group="evaporite",
        required_inputs=("phi_n", "dt", "vsh"),
        intercept=3.658284340892447,
        coefficients={"phi_n": -5.13, "dt": 0.00293, "vsh": -1.7},
        reference="Fuchs et al. (2015), Table 3, A67",
    ),

    "A68": Equation(
        id="A68",
        property="tc",
        rock_group="evaporite",
        required_inputs=("U", "dt", "vsh"),
        intercept=5.764417977766672,
        coefficients={"U": -0.018, "dt": -0.0087, "vsh": -2.01},
        reference="Fuchs et al. (2015), Table 3, A68",
    ),

    "A69": Equation(
        id="A69",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "dt", "vsh"),
        intercept=3.3389468776135156,
        coefficients={"rho_b": 0.681, "dt": -0.006, "vsh": -2.03},
        reference="Fuchs et al. (2015), Table 3, A69",
    ),

    "A70": Equation(
        id="A70",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "dt"),
        intercept=-7.9540095189495466,
        coefficients={"rho_b": 5.097, "U": -0.36, "dt": 0.0027},
        reference="Fuchs et al. (2015), Table 3, A70",
    ),

    "A71": Equation(
        id="A71",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "vsh"),
        intercept=-3.137278587413879,
        coefficients={"rho_b": 3.187, "U": -0.186, "vsh": -1.49},
        reference="Fuchs et al. (2015), Table 3, A71",
    ),

    "A72": Equation(
        id="A72",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=-10.01397812188739,
        coefficients={"rho_b": 4.361, "phi_n": -8.55, "U": -0.226, "dt": 0.02145},
        reference="Fuchs et al. (2015), Table 3, A72",
    ),

    "A73": Equation(
        id="A73",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "vsh"),
        intercept=0.3559774659031457,
        coefficients={"rho_b": 1.685, "phi_n": -2.09, "U": -0.1, "vsh": -1.59},
        reference="Fuchs et al. (2015), Table 3, A73",
    ),

    "A74": Equation(
        id="A74",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "dt", "vsh"),
        intercept=-1.5484146239157017,
        coefficients={"rho_b": 1.386, "phi_n": -6.81, "dt": 0.01152, "vsh": -1.53},
        reference="Fuchs et al. (2015), Table 3, A74",
    ),

    "A75": Equation(
        id="A75",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "dt", "vsh"),
        intercept=-1.0606841802358233,
        coefficients={"rho_b": 2.491, "U": -0.155, "dt": -0.0023, "vsh": -1.58},
        reference="Fuchs et al. (2015), Table 3, A75",
    ),

    "A76": Equation(
        id="A76",
        property="tc",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "dt", "vsh"),
        intercept=2.943589847518817,
        coefficients={"phi_n": -6.0, "U": 0.038, "dt": 0.00551, "vsh": -1.73},
        reference="Fuchs et al. (2015), Table 3, A76",
    ),

    "A77": Equation(
        id="A77",
        property="tc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "dt", "vsh"),
        intercept=-3.6008813542163325,
        coefficients={"rho_b": 2.416, "phi_n": -5.84, "U": -0.097, "dt": 0.01133, "vsh": -1.32},
        reference="Fuchs et al. (2015), Table 3, A77",
    ),

    "B1": Equation(
        id="B1",
        property="td",
        rock_group="clastic",
        required_inputs=("rho_b",),
        intercept=2.0943563772279155,
        coefficients={"rho_b": -0.27},
        reference="Fuchs et al. (2015), Table 3, B1",
    ),

    "B2": Equation(
        id="B2",
        property="td",
        rock_group="clastic",
        required_inputs=("phi_n",),
        intercept=2.487330763624223,
        coefficients={"phi_n": -4.354115683401195},
        reference="Fuchs et al. (2015), Table 3, B2",
    ),

    "B3": Equation(
        id="B3",
        property="td",
        rock_group="clastic",
        required_inputs=("U",),
        intercept=-1.246199992493112,
        coefficients={"U": 0.27},
        reference="Fuchs et al. (2015), Table 3, B3",
    ),

    "B4": Equation(
        id="B4",
        property="td",
        rock_group="clastic",
        required_inputs=("dt",),
        intercept=1.9148488898655187,
        coefficients={"dt": -0.0018},
        reference="Fuchs et al. (2015), Table 3, B4",
    ),

    "B5": Equation(
        id="B5",
        property="td",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n"),
        intercept=4.943082442236474,
        coefficients={"rho_b": -1.01, "phi_n": -4.84272625164719},
        reference="Fuchs et al. (2015), Table 3, B5",
    ),

    "B6": Equation(
        id="B6",
        property="td",
        rock_group="clastic",
        required_inputs=("rho_b", "U"),
        intercept=0.14022668451786968,
        coefficients={"rho_b": -0.69, "U": 0.29},
        reference="Fuchs et al. (2015), Table 3, B6",
    ),

    "B7": Equation(
        id="B7",
        property="td",
        rock_group="clastic",
        required_inputs=("rho_b", "dt"),
        intercept=8.499853618887826,
        coefficients={"rho_b": -1.9, "dt": -0.01065},
        reference="Fuchs et al. (2015), Table 3, B7",
    ),

    "B8": Equation(
        id="B8",
        property="td",
        rock_group="clastic",
        required_inputs=("phi_n", "U"),
        intercept=1.702700207948447,
        coefficients={"phi_n": -3.8305306744597485, "U": 0.07},
        reference="Fuchs et al. (2015), Table 3, B8",
    ),

    "B9": Equation(
        id="B9",
        property="td",
        rock_group="clastic",
        required_inputs=("phi_n", "dt"),
        intercept=1.7782945836045019,
        coefficients={"phi_n": -4.70729806416266, "dt": 0.00321},
        reference="Fuchs et al. (2015), Table 3, B9",
    ),

    "B10": Equation(
        id="B10",
        property="td",
        rock_group="clastic",
        required_inputs=("U", "dt"),
        intercept=-1.6861906123518433,
        coefficients={"U": 0.28, "dt": 0.00135},
        reference="Fuchs et al. (2015), Table 3, B10",
    ),

    "B11": Equation(
        id="B11",
        property="td",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=4.100170304550882,
        coefficients={"rho_b": -1.03, "phi_n": -4.25934075698068, "U": 0.07},
        reference="Fuchs et al. (2015), Table 3, B11",
    ),

    "B12": Equation(
        id="B12",
        property="td",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=7.830084887023768,
        coefficients={"rho_b": -1.75, "phi_n": -4.648036779159257, "dt": -0.00499},
        reference="Fuchs et al. (2015), Table 3, B12",
    ),

    "B13": Equation(
        id="B13",
        property="td",
        rock_group="clastic",
        required_inputs=("rho_b", "U", "dt"),
        intercept=4.144332615850178,
        coefficients={"rho_b": -1.65, "U": 0.27, "dt": -0.00642},
        reference="Fuchs et al. (2015), Table 3, B13",
    ),

    "B14": Equation(
        id="B14",
        property="td",
        rock_group="clastic",
        required_inputs=("phi_n", "U", "dt"),
        intercept=0.8027405823151523,
        coefficients={"phi_n": -4.118809290701103, "U": 0.08, "dt": 0.00345},
        reference="Fuchs et al. (2015), Table 3, B14",
    ),

    "B15": Equation(
        id="B15",
        property="td",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=6.856456664247608,
        coefficients={"rho_b": -1.7, "phi_n": -4.156440164317058, "U": 0.06, "dt": -0.00457},
        reference="Fuchs et al. (2015), Table 3, B15",
    ),

    "B16": Equation(
        id="B16",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b",),
        intercept=-2.6659504270958845,
        coefficients={"rho_b": 1.58},
        reference="Fuchs et al. (2015), Table 3, B16",
    ),

    "B17": Equation(
        id="B17",
        property="td",
        rock_group="carbonate",
        required_inputs=("phi_n",),
        intercept=1.8296398507844664,
        coefficients={"phi_n": -2.9475913766924013},
        reference="Fuchs et al. (2015), Table 3, B17",
    ),

    "B18": Equation(
        id="B18",
        property="td",
        rock_group="carbonate",
        required_inputs=("U",),
        intercept=0.571093191482408,
        coefficients={"U": 0.07},
        reference="Fuchs et al. (2015), Table 3, B18",
    ),

    "B19": Equation(
        id="B19",
        property="td",
        rock_group="carbonate",
        required_inputs=("dt",),
        intercept=2.791769243643087,
        coefficients={"dt": -0.00687},
        reference="Fuchs et al. (2015), Table 3, B19",
    ),

    "B20": Equation(
        id="B20",
        property="td",
        rock_group="carbonate",
        required_inputs=("vsh",),
        intercept=1.4523641597853707,
        coefficients={"vsh": -0.75},
        reference="Fuchs et al. (2015), Table 3, B20",
    ),

    "B21": Equation(
        id="B21",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n"),
        intercept=0.8638050232143356,
        coefficients={"rho_b": 0.36, "phi_n": -2.455397405403219},
        reference="Fuchs et al. (2015), Table 3, B21",
    ),

    "B22": Equation(
        id="B22",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "U"),
        intercept=-3.609714597949332,
        coefficients={"rho_b": 2.37, "U": -0.13},
        reference="Fuchs et al. (2015), Table 3, B22",
    ),

    "B23": Equation(
        id="B23",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "dt"),
        intercept=2.4106227461830185,
        coefficients={"rho_b": 0.12, "dt": -0.00645},
        reference="Fuchs et al. (2015), Table 3, B23",
    ),

    "B24": Equation(
        id="B24",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "vsh"),
        intercept=-2.1081116615479,
        coefficients={"rho_b": 1.42, "vsh": -0.35},
        reference="Fuchs et al. (2015), Table 3, B24",
    ),

    "B25": Equation(
        id="B25",
        property="td",
        rock_group="carbonate",
        required_inputs=("phi_n", "U"),
        intercept=2.339419514105273,
        coefficients={"phi_n": -3.373740535492348, "U": -0.06},
        reference="Fuchs et al. (2015), Table 3, B25",
    ),

    "B26": Equation(
        id="B26",
        property="td",
        rock_group="carbonate",
        required_inputs=("phi_n", "dt"),
        intercept=2.186870744146069,
        coefficients={"phi_n": -2.0133176709100327, "dt": -0.00239},
        reference="Fuchs et al. (2015), Table 3, B26",
    ),

    "B27": Equation(
        id="B27",
        property="td",
        rock_group="carbonate",
        required_inputs=("phi_n", "vsh"),
        intercept=1.8887763004745945,
        coefficients={"phi_n": -2.7591092514717066, "vsh": -0.21},
        reference="Fuchs et al. (2015), Table 3, B27",
    ),

    "B28": Equation(
        id="B28",
        property="td",
        rock_group="carbonate",
        required_inputs=("U", "dt"),
        intercept=3.6152644538864265,
        coefficients={"U": -0.07, "dt": -0.00821},
        reference="Fuchs et al. (2015), Table 3, B28",
    ),

    "B29": Equation(
        id="B29",
        property="td",
        rock_group="carbonate",
        required_inputs=("U", "vsh"),
        intercept=1.1424987655278709,
        coefficients={"U": 0.04, "vsh": -0.67},
        reference="Fuchs et al. (2015), Table 3, B29",
    ),

    "B30": Equation(
        id="B30",
        property="td",
        rock_group="carbonate",
        required_inputs=("dt", "vsh"),
        intercept=2.877087154496847,
        coefficients={"dt": -0.00632, "vsh": -0.44},
        reference="Fuchs et al. (2015), Table 3, B30",
    ),

    "B31": Equation(
        id="B31",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=-0.39269794529882374,
        coefficients={"rho_b": 1.18, "phi_n": -2.13812758538297, "U": -0.11},
        reference="Fuchs et al. (2015), Table 3, B31",
    ),

    "B32": Equation(
        id="B32",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=1.5819707074823275,
        coefficients={"rho_b": 0.18, "phi_n": -2.03736174559023, "dt": -0.00168},
        reference="Fuchs et al. (2015), Table 3, B32",
    ),

    "B33": Equation(
        id="B33",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "vsh"),
        intercept=0.9565360254734865,
        coefficients={"rho_b": 0.34, "phi_n": -2.2889223747397835, "vsh": -0.21},
        reference="Fuchs et al. (2015), Table 3, B33",
    ),

    "B34": Equation(
        id="B34",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "dt"),
        intercept=0.5289736285879587,
        coefficients={"rho_b": 1.09, "U": -0.11, "dt": -0.00505},
        reference="Fuchs et al. (2015), Table 3, B34",
    ),

    "B35": Equation(
        id="B35",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "vsh"),
        intercept=-3.000044141616669,
        coefficients={"rho_b": 2.23, "U": -0.14, "vsh": -0.43},
        reference="Fuchs et al. (2015), Table 3, B35",
    ),

    "B36": Equation(
        id="B36",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "dt", "vsh"),
        intercept=4.007040909432084,
        coefficients={"rho_b": -0.34, "dt": -0.0075, "vsh": -0.48},
        reference="Fuchs et al. (2015), Table 3, B36",
    ),

    "B37": Equation(
        id="B37",
        property="td",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "dt"),
        intercept=3.009661499807996,
        coefficients={"phi_n": -1.9923144527895664, "U": -0.07, "dt": -0.00376},
        reference="Fuchs et al. (2015), Table 3, B37",
    ),

    "B38": Equation(
        id="B38",
        property="td",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "vsh"),
        intercept=2.469693063925395,
        coefficients={"phi_n": -3.183580655252699, "U": -0.06, "vsh": -0.27},
        reference="Fuchs et al. (2015), Table 3, B38",
    ),

    "B39": Equation(
        id="B39",
        property="td",
        rock_group="carbonate",
        required_inputs=("phi_n", "dt", "vsh"),
        intercept=2.5911901305721488,
        coefficients={"phi_n": -0.8985329120783785, "dt": -0.00442, "vsh": -0.36},
        reference="Fuchs et al. (2015), Table 3, B39",
    ),

    "B40": Equation(
        id="B40",
        property="td",
        rock_group="carbonate",
        required_inputs=("U", "dt", "vsh"),
        intercept=4.015497211477495,
        coefficients={"U": -0.09, "dt": -0.00797, "vsh": -0.57},
        reference="Fuchs et al. (2015), Table 3, B40",
    ),

    "B41": Equation(
        id="B41",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=-0.3856065036724927,
        coefficients={"rho_b": 1.18, "phi_n": -2.134326446422818, "U": -0.11, "dt": -2e-05},
        reference="Fuchs et al. (2015), Table 3, B41",
    ),

    "B42": Equation(
        id="B42",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "vsh"),
        intercept=-0.3650848284253665,
        coefficients={"rho_b": 1.23, "phi_n": -1.8717935043378056, "U": -0.12, "vsh": -0.3},
        reference="Fuchs et al. (2015), Table 3, B42",
    ),

    "B43": Equation(
        id="B43",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "dt", "vsh"),
        intercept=3.4485640878573247,
        coefficients={"rho_b": -0.24, "phi_n": -0.7321947144904444, "dt": -0.00561, "vsh": -0.41},
        reference="Fuchs et al. (2015), Table 3, B43",
    ),

    "B44": Equation(
        id="B44",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "dt", "vsh"),
        intercept=2.123063605204992,
        coefficients={"rho_b": 0.65, "U": -0.11, "dt": -0.00609, "vsh": -0.52},
        reference="Fuchs et al. (2015), Table 3, B44",
    ),

    "B45": Equation(
        id="B45",
        property="td",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "dt", "vsh"),
        intercept=3.8924066829047956,
        coefficients={"phi_n": -0.3298524198614268, "U": -0.09, "dt": -0.00725, "vsh": -0.54},
        reference="Fuchs et al. (2015), Table 3, B45",
    ),

    "B46": Equation(
        id="B46",
        property="td",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "dt", "vsh"),
        intercept=1.59233333596561,
        coefficients={"rho_b": 0.75, "phi_n": -0.6997644742627042, "U": -0.11, "dt": -0.00429, "vsh": -0.45},
        reference="Fuchs et al. (2015), Table 3, B46",
    ),

    "B47": Equation(
        id="B47",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b",),
        intercept=-2.4200018751801275,
        coefficients={"rho_b": 1.44},
        reference="Fuchs et al. (2015), Table 3, B47",
    ),

    "B48": Equation(
        id="B48",
        property="td",
        rock_group="evaporite",
        required_inputs=("phi_n",),
        intercept=1.6949028324042315,
        coefficients={"phi_n": -3.088243661875065},
        reference="Fuchs et al. (2015), Table 3, B48",
    ),

    "B49": Equation(
        id="B49",
        property="td",
        rock_group="evaporite",
        required_inputs=("U",),
        intercept=0.8430977276582697,
        coefficients={"U": 0.02},
        reference="Fuchs et al. (2015), Table 3, B49",
    ),

    "B50": Equation(
        id="B50",
        property="td",
        rock_group="evaporite",
        required_inputs=("dt",),
        intercept=2.682028676572912,
        coefficients={"dt": -0.00659},
        reference="Fuchs et al. (2015), Table 3, B50",
    ),

    "B51": Equation(
        id="B51",
        property="td",
        rock_group="evaporite",
        required_inputs=("vsh",),
        intercept=1.5419962271430399,
        coefficients={"vsh": -0.97},
        reference="Fuchs et al. (2015), Table 3, B51",
    ),

    "B52": Equation(
        id="B52",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n"),
        intercept=1.6647858886207374,
        coefficients={"rho_b": 0.01, "phi_n": -3.072750592194038},
        reference="Fuchs et al. (2015), Table 3, B52",
    ),

    "B53": Equation(
        id="B53",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "U"),
        intercept=-3.7906636153822406,
        coefficients={"rho_b": 2.58, "U": -0.19},
        reference="Fuchs et al. (2015), Table 3, B53",
    ),

    "B54": Equation(
        id="B54",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "dt"),
        intercept=2.4346999196135544,
        coefficients={"rho_b": 0.08, "dt": -0.00633},
        reference="Fuchs et al. (2015), Table 3, B54",
    ),

    "B55": Equation(
        id="B55",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "vsh"),
        intercept=-1.6356634195855841,
        coefficients={"rho_b": 1.29, "vsh": -0.78},
        reference="Fuchs et al. (2015), Table 3, B55",
    ),

    "B56": Equation(
        id="B56",
        property="td",
        rock_group="evaporite",
        required_inputs=("phi_n", "U"),
        intercept=2.041230017992742,
        coefficients={"phi_n": -3.275621797274233, "U": -0.04},
        reference="Fuchs et al. (2015), Table 3, B56",
    ),

    "B57": Equation(
        id="B57",
        property="td",
        rock_group="evaporite",
        required_inputs=("phi_n", "dt"),
        intercept=0.9377962486841336,
        coefficients={"phi_n": -4.990882735867, "dt": 0.00465},
        reference="Fuchs et al. (2015), Table 3, B57",
    ),

    "B58": Equation(
        id="B58",
        property="td",
        rock_group="evaporite",
        required_inputs=("phi_n", "vsh"),
        intercept=1.9490092757816408,
        coefficients={"phi_n": -2.772451482431609, "vsh": -0.6},
        reference="Fuchs et al. (2015), Table 3, B58",
    ),

    "B59": Equation(
        id="B59",
        property="td",
        rock_group="evaporite",
        required_inputs=("U", "dt"),
        intercept=3.561402618474106,
        coefficients={"U": -0.08, "dt": -0.00783},
        reference="Fuchs et al. (2015), Table 3, B59",
    ),

    "B60": Equation(
        id="B60",
        property="td",
        rock_group="evaporite",
        required_inputs=("U", "vsh"),
        intercept=1.17040989546055,
        coefficients={"U": 0.06, "vsh": -1.09},
        reference="Fuchs et al. (2015), Table 3, B60",
    ),

    "B61": Equation(
        id="B61",
        property="td",
        rock_group="evaporite",
        required_inputs=("dt", "vsh"),
        intercept=2.9805696365963232,
        coefficients={"dt": -0.00608, "vsh": -0.79},
        reference="Fuchs et al. (2015), Table 3, B61",
    ),

    "B62": Equation(
        id="B62",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=-1.2095148309623367,
        coefficients={"rho_b": 1.48, "phi_n": -1.6224938195252225, "U": -0.13},
        reference="Fuchs et al. (2015), Table 3, B62",
    ),

    "B63": Equation(
        id="B63",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=-1.0299610624408617,
        coefficients={"rho_b": 0.55, "phi_n": -5.430701211357951, "dt": 0.0076},
        reference="Fuchs et al. (2015), Table 3, B63",
    ),

    "B64": Equation(
        id="B64",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "vsh"),
        intercept=1.6724428287474513,
        coefficients={"rho_b": 0.1, "phi_n": -2.6266751327621796, "vsh": -0.6},
        reference="Fuchs et al. (2015), Table 3, B64",
    ),

    "B65": Equation(
        id="B65",
        property="td",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "dt"),
        intercept=1.530941404262126,
        coefficients={"phi_n": -4.23153914458418, "U": -0.03, "dt": 0.00248},
        reference="Fuchs et al. (2015), Table 3, B65",
    ),

    "B66": Equation(
        id="B66",
        property="td",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "vsh"),
        intercept=2.05705004323642,
        coefficients={"phi_n": -2.862366536301357, "U": -0.02, "vsh": -0.55},
        reference="Fuchs et al. (2015), Table 3, B66",
    ),

    "B67": Equation(
        id="B67",
        property="td",
        rock_group="evaporite",
        required_inputs=("phi_n", "dt", "vsh"),
        intercept=1.837448367832669,
        coefficients={"phi_n": -3.043362978545231, "dt": 0.00064, "vsh": -0.58},
        reference="Fuchs et al. (2015), Table 3, B67",
    ),

    "B68": Equation(
        id="B68",
        property="td",
        rock_group="evaporite",
        required_inputs=("U", "dt", "vsh"),
        intercept=3.4135917267942575,
        coefficients={"U": -0.04, "dt": -0.00681, "vsh": -0.69},
        reference="Fuchs et al. (2015), Table 3, B68",
    ),

    "B69": Equation(
        id="B69",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "dt", "vsh"),
        intercept=3.2937669153045093,
        coefficients={"rho_b": -0.09, "dt": -0.00641, "vsh": -0.79},
        reference="Fuchs et al. (2015), Table 3, B69",
    ),

    "B70": Equation(
        id="B70",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "dt"),
        intercept=-1.821792073443005,
        coefficients={"rho_b": 1.94, "U": -0.17, "dt": -0.00236},
        reference="Fuchs et al. (2015), Table 3, B70",
    ),

    "B71": Equation(
        id="B71",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "dt", "vsh"),
        intercept=-3.2086464499388123,
        coefficients={"rho_b": 2.31, "U": -0.16, "dt": 0.00493, "vsh": -0.34},
        reference="Fuchs et al. (2015), Table 3, B71",
    ),

    "B72": Equation(
        id="B72",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=-2.6221079528190523,
        coefficients={"rho_b": 1.65, "phi_n": -3.322563558541464, "U": -0.12, "dt": 0.00493},
        reference="Fuchs et al. (2015), Table 3, B72",
    ),

    "B73": Equation(
        id="B73",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "vsh"),
        intercept=-0.08019440509314296,
        coefficients={"rho_b": 0.97, "phi_n": -1.8731687715568237, "U": -0.08, "vsh": -0.43},
        reference="Fuchs et al. (2015), Table 3, B73",
    ),

    "B74": Equation(
        id="B74",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "dt", "vsh"),
        intercept=0.891808167654548,
        coefficients={"rho_b": 0.25, "phi_n": -3.348690266298839, "dt": 0.0022, "vsh": -0.55},
        reference="Fuchs et al. (2015), Table 3, B74",
    ),

    "B75": Equation(
        id="B75",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "dt", "vsh"),
        intercept=0.3143506108742104,
        coefficients={"rho_b": 1.13, "U": -0.11, "dt": -0.00391, "vsh": -0.49},
        reference="Fuchs et al. (2015), Table 3, B75",
    ),

    "B76": Equation(
        id="B76",
        property="td",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "dt", "vsh"),
        intercept=2.1807992927122544,
        coefficients={"phi_n": -2.624311387642102, "U": -0.02, "dt": -0.0006, "vsh": -0.56},
        reference="Fuchs et al. (2015), Table 3, B76",
    ),

    "B77": Equation(
        id="B77",
        property="td",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "dt", "vsh"),
        intercept=-0.794549942310347,
        coefficients={"rho_b": 1.1, "phi_n": -2.550236563100917, "U": -0.08, "dt": 0.00205, "vsh": -0.38},
        reference="Fuchs et al. (2015), Table 3, B77",
    ),

    "C1": Equation(
        id="C1",
        property="shc",
        rock_group="clastic",
        required_inputs=("rho_b",),
        intercept=2973.7161647845032,
        coefficients={"rho_b": -708.2},
        reference="Fuchs et al. (2015), Table 3, C1",
    ),

    "C2": Equation(
        id="C2",
        property="shc",
        rock_group="clastic",
        required_inputs=("phi_n",),
        intercept=1012.5007410045861,
        coefficients={"phi_n": 1382.1},
        reference="Fuchs et al. (2015), Table 3, C2",
    ),

    "C3": Equation(
        id="C3",
        property="shc",
        rock_group="clastic",
        required_inputs=("U",),
        intercept=2412.546317984875,
        coefficients={"U": -107.9},
        reference="Fuchs et al. (2015), Table 3, C3",
    ),

    "C4": Equation(
        id="C4",
        property="shc",
        rock_group="clastic",
        required_inputs=("dt",),
        intercept=54.08431668346975,
        coefficients={"dt": 5.188},
        reference="Fuchs et al. (2015), Table 3, C4",
    ),

    "C5": Equation(
        id="C5",
        property="shc",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n"),
        intercept=2312.9134696825895,
        coefficients={"rho_b": -535.9, "phi_n": 1123.3},
        reference="Fuchs et al. (2015), Table 3, C5",
    ),

    "C6": Equation(
        id="C6",
        property="shc",
        rock_group="clastic",
        required_inputs=("rho_b", "U"),
        intercept=3573.6215982261447,
        coefficients={"rho_b": -578.7, "U": -90.0},
        reference="Fuchs et al. (2015), Table 3, C6",
    ),

    "C7": Equation(
        id="C7",
        property="shc",
        rock_group="clastic",
        required_inputs=("rho_b", "dt"),
        intercept=-1002.073993579534,
        coefficients={"rho_b": 305.0, "dt": 6.607},
        reference="Fuchs et al. (2015), Table 3, C7",
    ),

    "C8": Equation(
        id="C8",
        property="shc",
        rock_group="clastic",
        required_inputs=("phi_n", "U"),
        intercept=1703.5901161013683,
        coefficients={"phi_n": 920.9, "U": -58.4},
        reference="Fuchs et al. (2015), Table 3, C8",
    ),

    "C9": Equation(
        id="C9",
        property="shc",
        rock_group="clastic",
        required_inputs=("phi_n", "dt"),
        intercept=80.71285403535933,
        coefficients={"phi_n": 917.9, "dt": 4.213},
        reference="Fuchs et al. (2015), Table 3, C9",
    ),

    "C10": Equation(
        id="C10",
        property="shc",
        rock_group="clastic",
        required_inputs=("U", "dt"),
        intercept=991.0536429177087,
        coefficients={"U": -73.5, "dt": 4.369},
        reference="Fuchs et al. (2015), Table 3, C10",
    ),

    "C11": Equation(
        id="C11",
        property="shc",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=2919.658355372215,
        coefficients={"rho_b": -522.6, "phi_n": 703.4, "U": -54.0},
        reference="Fuchs et al. (2015), Table 3, C11",
    ),

    "C12": Equation(
        id="C12",
        property="shc",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=-871.1448071709433,
        coefficients={"rho_b": 274.8, "phi_n": 908.6, "dt": 5.502},
        reference="Fuchs et al. (2015), Table 3, C12",
    ),

    "C13": Equation(
        id="C13",
        property="shc",
        rock_group="clastic",
        required_inputs=("rho_b", "U", "dt"),
        intercept=150.50755714360878,
        coefficients={"rho_b": 237.2, "U": -72.0, "dt": 5.49},
        reference="Fuchs et al. (2015), Table 3, C13",
    ),

    "C14": Equation(
        id="C14",
        property="shc",
        rock_group="clastic",
        required_inputs=("phi_n", "U", "dt"),
        intercept=640.3657444446621,
        coefficients={"phi_n": 580.3, "U": -44.7, "dt": 4.074},
        reference="Fuchs et al. (2015), Table 3, C14",
    ),

    "C15": Equation(
        id="C15",
        property="shc",
        rock_group="clastic",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=-231.7054968793325,
        coefficients={"rho_b": 245.2, "phi_n": 585.8, "U": -42.9, "dt": 5.23},
        reference="Fuchs et al. (2015), Table 3, C15",
    ),

    "C16": Equation(
        id="C16",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b",),
        intercept=4771.707392094608,
        coefficients={"rho_b": -1463.9},
        reference="Fuchs et al. (2015), Table 3, C16",
    ),

    "C17": Equation(
        id="C17",
        property="shc",
        rock_group="carbonate",
        required_inputs=("phi_n",),
        intercept=636.5676798561731,
        coefficients={"phi_n": 2625.3},
        reference="Fuchs et al. (2015), Table 3, C17",
    ),

    "C18": Equation(
        id="C18",
        property="shc",
        rock_group="carbonate",
        required_inputs=("U",),
        intercept=2014.4820859395254,
        coefficients={"U": -98.3},
        reference="Fuchs et al. (2015), Table 3, C18",
    ),

    "C19": Equation(
        id="C19",
        property="shc",
        rock_group="carbonate",
        required_inputs=("dt",),
        intercept=-376.71458073692224,
        coefficients={"dt": 6.747},
        reference="Fuchs et al. (2015), Table 3, C19",
    ),

    "C20": Equation(
        id="C20",
        property="shc",
        rock_group="carbonate",
        required_inputs=("vsh",),
        intercept=1292.8474599424228,
        coefficients={"vsh": 30.9},
        reference="Fuchs et al. (2015), Table 3, C20",
    ),

    "C21": Equation(
        id="C21",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n"),
        intercept=1987.0969992791306,
        coefficients={"rho_b": -496.4, "phi_n": 1937.1},
        reference="Fuchs et al. (2015), Table 3, C21",
    ),

    "C22": Equation(
        id="C22",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "U"),
        intercept=5138.018874982522,
        coefficients={"rho_b": -1769.2, "U": 49.6},
        reference="Fuchs et al. (2015), Table 3, C22",
    ),

    "C23": Equation(
        id="C23",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "dt"),
        intercept=-1555.3666262393117,
        coefficients={"rho_b": 361.4, "dt": 8.044},
        reference="Fuchs et al. (2015), Table 3, C23",
    ),

    "C24": Equation(
        id="C24",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "vsh"),
        intercept=5466.694718672172,
        coefficients={"rho_b": -1664.8, "vsh": -436.5},
        reference="Fuchs et al. (2015), Table 3, C24",
    ),

    "C25": Equation(
        id="C25",
        property="shc",
        rock_group="carbonate",
        required_inputs=("phi_n", "U"),
        intercept=639.9213912583654,
        coefficients={"phi_n": 2622.5, "U": -0.4},
        reference="Fuchs et al. (2015), Table 3, C25",
    ),

    "C26": Equation(
        id="C26",
        property="shc",
        rock_group="carbonate",
        required_inputs=("phi_n", "dt"),
        intercept=-411.4527180757507,
        coefficients={"phi_n": -115.6, "dt": 7.005},
        reference="Fuchs et al. (2015), Table 3, C26",
    ),

    "C27": Equation(
        id="C27",
        property="shc",
        rock_group="carbonate",
        required_inputs=("phi_n", "vsh"),
        intercept=796.8158127517546,
        coefficients={"phi_n": 3136.0, "vsh": -578.1},
        reference="Fuchs et al. (2015), Table 3, C27",
    ),

    "C28": Equation(
        id="C28",
        property="shc",
        rock_group="carbonate",
        required_inputs=("U", "dt"),
        intercept=-654.7093261712623,
        coefficients={"U": 23.0, "dt": 7.199},
        reference="Fuchs et al. (2015), Table 3, C28",
    ),

    "C29": Equation(
        id="C29",
        property="shc",
        rock_group="carbonate",
        required_inputs=("U", "vsh"),
        intercept=2194.521950881098,
        coefficients={"U": -108.6, "vsh": -210.0},
        reference="Fuchs et al. (2015), Table 3, C29",
    ),

    "C30": Equation(
        id="C30",
        property="shc",
        rock_group="carbonate",
        required_inputs=("dt", "vsh"),
        intercept=-316.7268681394687,
        coefficients={"dt": 7.138, "vsh": -312.8},
        reference="Fuchs et al. (2015), Table 3, C30",
    ),

    "C31": Equation(
        id="C31",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=2368.3993134248876,
        coefficients={"rho_b": -747.0, "phi_n": 1840.8, "U": 32.9},
        reference="Fuchs et al. (2015), Table 3, C31",
    ),

    "C32": Equation(
        id="C32",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=-1621.9631604951358,
        coefficients={"rho_b": 366.7, "phi_n": -163.7, "dt": 8.427},
        reference="Fuchs et al. (2015), Table 3, C32",
    ),

    "C33": Equation(
        id="C33",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "vsh"),
        intercept=2247.4249602768937,
        coefficients={"rho_b": -532.4, "phi_n": 2404.4, "vsh": -585.5},
        reference="Fuchs et al. (2015), Table 3, C33",
    ),

    "C34": Equation(
        id="C34",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "dt"),
        intercept=-1281.5180150877814,
        coefficients={"rho_b": 220.4, "U": 15.4, "dt": 7.84},
        reference="Fuchs et al. (2015), Table 3, C34",
    ),

    "C35": Equation(
        id="C35",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "vsh"),
        intercept=5728.692667183341,
        coefficients={"rho_b": -1902.7, "U": 40.3, "vsh": -413.9},
        reference="Fuchs et al. (2015), Table 3, C35",
    ),

    "C36": Equation(
        id="C36",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "dt", "vsh"),
        intercept=-551.707475024258,
        coefficients={"rho_b": 71.6, "dt": 7.384, "vsh": -304.6},
        reference="Fuchs et al. (2015), Table 3, C36",
    ),

    "C37": Equation(
        id="C37",
        property="shc",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "dt"),
        intercept=-692.0316753888983,
        coefficients={"phi_n": -122.8, "U": 23.0, "dt": 7.473},
        reference="Fuchs et al. (2015), Table 3, C37",
    ),

    "C38": Equation(
        id="C38",
        property="shc",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "vsh"),
        intercept=926.7172500346742,
        coefficients={"phi_n": 3041.1, "U": -13.8, "vsh": -590.3},
        reference="Fuchs et al. (2015), Table 3, C38",
    ),

    "C39": Equation(
        id="C39",
        property="shc",
        rock_group="carbonate",
        required_inputs=("phi_n", "dt", "vsh"),
        intercept=60.687548947247365,
        coefficients={"phi_n": 1186.1, "dt": 4.632, "vsh": -422.5},
        reference="Fuchs et al. (2015), Table 3, C39",
    ),

    "C40": Equation(
        id="C40",
        property="shc",
        rock_group="carbonate",
        required_inputs=("U", "dt", "vsh"),
        intercept=-444.8193053583167,
        coefficients={"U": 10.4, "dt": 7.324, "vsh": -298.7},
        reference="Fuchs et al. (2015), Table 3, C40",
    ),

    "C41": Equation(
        id="C41",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=-1345.8502517146253,
        coefficients={"rho_b": 227.0, "phi_n": -150.1, "U": 15.2, "dt": 8.194},
        reference="Fuchs et al. (2015), Table 3, C41",
    ),

    "C42": Equation(
        id="C42",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "vsh"),
        intercept=2421.1510696356586,
        coefficients={"rho_b": -649.4, "phi_n": 2349.6, "U": 15.4, "vsh": -573.4},
        reference="Fuchs et al. (2015), Table 3, C42",
    ),

    "C43": Equation(
        id="C43",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "dt", "vsh"),
        intercept=403.80118637718954,
        coefficients={"rho_b": -98.0, "phi_n": 1252.7, "dt": 4.154, "vsh": -439.9},
        reference="Fuchs et al. (2015), Table 3, C43",
    ),

    "C44": Equation(
        id="C44",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "U", "dt", "vsh"),
        intercept=-363.69822795929406,
        coefficients={"rho_b": -28.0, "U": 11.3, "dt": 7.243, "vsh": -300.8},
        reference="Fuchs et al. (2015), Table 3, C44",
    ),

    "C45": Equation(
        id="C45",
        property="shc",
        rock_group="carbonate",
        required_inputs=("phi_n", "U", "dt", "vsh"),
        intercept=-14.433624498934535,
        coefficients={"phi_n": 1153.3, "U": 5.2, "dt": 4.795, "vsh": -412.3},
        reference="Fuchs et al. (2015), Table 3, C45",
    ),

    "C46": Equation(
        id="C46",
        property="shc",
        rock_group="carbonate",
        required_inputs=("rho_b", "phi_n", "U", "dt", "vsh"),
        intercept=584.03263413829,
        coefficients={"rho_b": -194.4, "phi_n": 1249.6, "U": 10.9, "dt": 4.025, "vsh": -435.9},
        reference="Fuchs et al. (2015), Table 3, C46",
    ),

    "C47": Equation(
        id="C47",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b",),
        intercept=4969.132085247719,
        coefficients={"rho_b": -1558.9},
        reference="Fuchs et al. (2015), Table 3, C47",
    ),

    "C48": Equation(
        id="C48",
        property="shc",
        rock_group="evaporite",
        required_inputs=("phi_n",),
        intercept=579.887511880365,
        coefficients={"phi_n": 3007.8},
        reference="Fuchs et al. (2015), Table 3, C48",
    ),

    "C49": Equation(
        id="C49",
        property="shc",
        rock_group="evaporite",
        required_inputs=("U",),
        intercept=1968.4835364606286,
        coefficients={"U": -101.8},
        reference="Fuchs et al. (2015), Table 3, C49",
    ),

    "C50": Equation(
        id="C50",
        property="shc",
        rock_group="evaporite",
        required_inputs=("dt",),
        intercept=-591.9606453611082,
        coefficients={"dt": 7.253},
        reference="Fuchs et al. (2015), Table 3, C50",
    ),

    "C51": Equation(
        id="C51",
        property="shc",
        rock_group="evaporite",
        required_inputs=("vsh",),
        intercept=1228.8746376342158,
        coefficients={"vsh": 27.2},
        reference="Fuchs et al. (2015), Table 3, C51",
    ),

    "C52": Equation(
        id="C52",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n"),
        intercept=1815.8391286075887,
        coefficients={"rho_b": -458.5, "phi_n": 2372.0},
        reference="Fuchs et al. (2015), Table 3, C52",
    ),

    "C53": Equation(
        id="C53",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "U"),
        intercept=5370.905744850537,
        coefficients={"rho_b": -1893.8, "U": 56.0},
        reference="Fuchs et al. (2015), Table 3, C53",
    ),

    "C54": Equation(
        id="C54",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "dt"),
        intercept=-617.691989541187,
        coefficients={"rho_b": 7.8, "dt": 7.281},
        reference="Fuchs et al. (2015), Table 3, C54",
    ),

    "C55": Equation(
        id="C55",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "vsh"),
        intercept=5176.220918043206,
        coefficients={"rho_b": -1598.4, "vsh": -206.8},
        reference="Fuchs et al. (2015), Table 3, C55",
    ),

    "C56": Equation(
        id="C56",
        property="shc",
        rock_group="evaporite",
        required_inputs=("phi_n", "U"),
        intercept=939.4514847386856,
        coefficients={"phi_n": 2813.3, "U": -44.5},
        reference="Fuchs et al. (2015), Table 3, C56",
    ),

    "C57": Equation(
        id="C57",
        property="shc",
        rock_group="evaporite",
        required_inputs=("phi_n", "dt"),
        intercept=-411.2363676836842,
        coefficients={"phi_n": 517.1, "dt": 6.088},
        reference="Fuchs et al. (2015), Table 3, C57",
    ),

    "C58": Equation(
        id="C58",
        property="shc",
        rock_group="evaporite",
        required_inputs=("phi_n", "vsh"),
        intercept=755.3003268536772,
        coefficients={"phi_n": 3225.8, "vsh": -410.7},
        reference="Fuchs et al. (2015), Table 3, C58",
    ),

    "C59": Equation(
        id="C59",
        property="shc",
        rock_group="evaporite",
        required_inputs=("U", "dt"),
        intercept=-507.1691864590403,
        coefficients={"U": -7.7, "dt": 7.133},
        reference="Fuchs et al. (2015), Table 3, C59",
    ),

    "C60": Equation(
        id="C60",
        property="shc",
        rock_group="evaporite",
        required_inputs=("U", "vsh"),
        intercept=1898.3494734158692,
        coefficients={"U": -109.8, "vsh": 232.6},
        reference="Fuchs et al. (2015), Table 3, C60",
    ),

    "C61": Equation(
        id="C61",
        property="shc",
        rock_group="evaporite",
        required_inputs=("dt", "vsh"),
        intercept=-517.5216842154234,
        coefficients={"dt": 7.381, "vsh": -196.3},
        reference="Fuchs et al. (2015), Table 3, C61",
    ),

    "C62": Equation(
        id="C62",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U"),
        intercept=708.4937585322632,
        coefficients={"rho_b": 104.6, "phi_n": 2930.8, "U": -50.8},
        reference="Fuchs et al. (2015), Table 3, C62",
    ),

    "C63": Equation(
        id="C63",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "dt"),
        intercept=-267.25116631882577,
        coefficients={"rho_b": -40.4, "phi_n": 549.3, "dt": 5.872},
        reference="Fuchs et al. (2015), Table 3, C63",
    ),

    "C64": Equation(
        id="C64",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "vsh"),
        intercept=1820.8540891254431,
        coefficients={"rho_b": -398.1, "phi_n": 2664.2, "vsh": -392.8},
        reference="Fuchs et al. (2015), Table 3, C64",
    ),

    "C65": Equation(
        id="C65",
        property="shc",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "dt"),
        intercept=-16.636632692958855,
        coefficients={"phi_n": 1022.3, "U": -19.7, "dt": 4.642},
        reference="Fuchs et al. (2015), Table 3, C65",
    ),

    "C66": Equation(
        id="C66",
        property="shc",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "vsh"),
        intercept=949.0705927987347,
        coefficients={"phi_n": 3064.6, "U": -27.9, "vsh": -336.7},
        reference="Fuchs et al. (2015), Table 3, C66",
    ),

    "C67": Equation(
        id="C67",
        property="shc",
        rock_group="evaporite",
        required_inputs=("phi_n", "dt", "vsh"),
        intercept=59.34454793252139,
        coefficients={"phi_n": 1535.8, "dt": 3.989, "vsh": -302.1},
        reference="Fuchs et al. (2015), Table 3, C67",
    ),

    "C68": Equation(
        id="C68",
        property="shc",
        rock_group="evaporite",
        required_inputs=("U", "dt", "vsh"),
        intercept=-551.213759231803,
        coefficients={"U": 3.3, "dt": 7.438, "vsh": -204.2},
        reference="Fuchs et al. (2015), Table 3, C68",
    ),

    "C69": Equation(
        id="C69",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "dt", "vsh"),
        intercept=-403.0122553583485,
        coefficients={"rho_b": -34.7, "dt": 7.259, "vsh": -197.7},
        reference="Fuchs et al. (2015), Table 3, C69",
    ),

    "C70": Equation(
        id="C70",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "dt"),
        intercept=-1029.468252863043,
        coefficients={"rho_b": 188.1, "U": -16.3, "dt": 7.664},
        reference="Fuchs et al. (2015), Table 3, C70",
    ),

    "C71": Equation(
        id="C71",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "vsh"),
        intercept=6243.793976182656,
        coefficients={"rho_b": -2294.3, "U": 106.7, "vsh": -508.2},
        reference="Fuchs et al. (2015), Table 3, C71",
    ),

    "C72": Equation(
        id="C72",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "dt"),
        intercept=-744.837126220765,
        coefficients={"rho_b": 289.8, "phi_n": 1181.7, "U": -34.9, "dt": 5.072},
        reference="Fuchs et al. (2015), Table 3, C72",
    ),

    "C73": Equation(
        id="C73",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "vsh"),
        intercept=1726.3549048632003,
        coefficients={"rho_b": -351.6, "phi_n": 2704.8, "U": -4.3, "vsh": -383.4},
        reference="Fuchs et al. (2015), Table 3, C73",
    ),

    "C74": Equation(
        id="C74",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "dt", "vsh"),
        intercept=891.2649541293255,
        coefficients={"rho_b": -221.4, "phi_n": 1804.4, "dt": 2.618, "vsh": -329.5},
        reference="Fuchs et al. (2015), Table 3, C74",
    ),

    "C75": Equation(
        id="C75",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "U", "dt", "vsh"),
        intercept=14.258094454249708,
        coefficients={"rho_b": -206.4, "U": 14.7, "dt": 6.908, "vsh": -239.8},
        reference="Fuchs et al. (2015), Table 3, C75",
    ),

    "C76": Equation(
        id="C76",
        property="shc",
        rock_group="evaporite",
        required_inputs=("phi_n", "U", "dt", "vsh"),
        intercept=319.2634475660111,
        coefficients={"phi_n": 1853.0, "U": -13.9, "dt": 3.052, "vsh": -290.9},
        reference="Fuchs et al. (2015), Table 3, C76",
    ),

    "C77": Equation(
        id="C77",
        property="shc",
        rock_group="evaporite",
        required_inputs=("rho_b", "phi_n", "U", "dt", "vsh"),
        intercept=814.6355132036576,
        coefficients={"rho_b": -182.9, "phi_n": 1840.7, "U": -3.6, "dt": 2.611, "vsh": -321.8},
        reference="Fuchs et al. (2015), Table 3, C77",
    ),
}


# -------------------------
# Access helpers
# -------------------------
def get_equation(equation_id: str) -> Equation:
    try:
        return EQUATIONS[equation_id]
    except KeyError:
        raise KeyError(f"Unknown equation: {equation_id}")


def list_equations() -> List[Equation]:
    return list(EQUATIONS.values())


def list_by_property(prop: str) -> List[Equation]:
    """Return all equations for a given property: 'tc', 'td', or 'shc'."""
    return [eq for eq in EQUATIONS.values() if eq.property == prop]


def list_by_rock_group(rock_group: str) -> List[Equation]:
    """Return all equations for a given rock group: 'clastic', 'carbonate', or 'evaporite'."""
    return [eq for eq in EQUATIONS.values() if eq.rock_group == rock_group]