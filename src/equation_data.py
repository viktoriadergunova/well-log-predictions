"""
All TC, TD, and SHC regression equations from Fuchs et al. (2015).

Equations are indexed in EQUATIONS and accessible via the helper
functions below.  The Equation class itself lives in :mod:`wellog.equation`.
"""

from __future__ import annotations

from typing import List

from .equation import Equation


EQUATIONS: dict[str, Equation] = {
    "A1": Equation(
        id="A1",
        property="tc",
        rock_group="evaporite",
        required_inputs=("RHOB",),
        intercept=5.31,
        coefficients={"RHOB": -0.809},
        rms=68.7,
        reference="Fuchs et al. (2015), Table 3, A1",

    ),

    "A2": Equation(
        id="A2",
        property="tc",
        rock_group="evaporite",
        required_inputs=("PHIN,"),
        intercept=5.34,
        coefficients={"PHIN": -8.14},
        rms=23.1,
        reference="Fuchs et al. (2015), Table 3, A2",
    ),

    "A3": Equation(
        id="A3",
        property="tc",
        rock_group="evaporite",
        required_inputs=("U"),
        intercept=-0.93,
        coefficients={"U": 0.437},
        rms=48.7,
        reference="Fuchs et al. (2015), Table 3, A3",
    ),

    "A4": Equation(
        id="A4",
        property="tc",
        rock_group="evaporite",
        required_inputs=("DT",),
        intercept=3.73,
        coefficients={"DT": -0.00117},
        rms=65.9,
        reference="Fuchs et al. (2015), Table 3, A4",
    ),

    "A5": Equation(
        id="A5",
        property="tc",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN"),
        intercept=10.73,
        coefficients={"RHOB": -2.223, "PHIN": -9.21},
        rms=15.8,   
        reference="Fuchs et al. (2015), Table 3, A5",
    ),

    "A6": Equation(
        id="A6",
        property="tc",
        rock_group="evaporite",
        required_inputs=("RHOB", "U"),
        intercept=2.09,
        coefficients={"RHOB": -1.504, "U": 0.483},
        rms=49.5,      
        reference="Fuchs et al. (2015), Table 3, A6",
    ),

    "A7": Equation(
        id="A7",
        property="tc",
        rock_group="evaporite",
        required_inputs=("RHOB", "DT"),
        intercept=15.69,
        coefficients={"RHOB": -3.455, "DT": -0.01725},
        rms=74.1,
        reference="Fuchs et al. (2015), Table 3, A7",
    ),

    "A8": Equation(
        id="A8",
        property="tc",
        rock_group="evaporite",
        required_inputs=("PHIN", "U"),
        intercept=5.34,
        coefficients={"PHIN": -8.14, "U": 0.0},
        rms=23.1,
        reference="Fuchs et al. (2015), Table 3, A8",
    ),

    "A9": Equation(
        id="A9",
        property="tc",
        rock_group="evaporite",
        required_inputs=("PHIN", "DT"),
        intercept=3.46,
        coefficients={"PHIN": -9.07, "DT": 0.00847},
        rms=22.6,
        reference="Fuchs et al. (2015), Table 3, A9",
    ),

    "A10": Equation(
        id="A10",
        property="tc",
        rock_group="evaporite",
        required_inputs=("U", "DT"),
        intercept=-2.25,
        coefficients={"U": 0.469, "DT": 0.00405},
        rms=47.6,
        reference="Fuchs et al. (2015), Table 3, A10",
    ),

    "A11": Equation(
        id="A11",
        property="tc",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=10.52,
        coefficients={"RHOB": -2.227, "PHIN": -9.07, "U": 0.019},
        rms=15.8,
        reference="Fuchs et al. (2015), Table 3, A11",
    ),

    "A12": Equation(
        id="A12",
        property="tc",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=14.40,
        coefficients={"RHOB": -3.157, "PHIN": -8.97, "DT": -0.00634},
        rms=14.8,
        reference="Fuchs et al. (2015), Table 3, A12",
    ),

    "A13": Equation(
        id="A13",
        property="tc",
        rock_group="evaporite",
        required_inputs=("RHOB", "U", "DT"),
        intercept=8.50,
        coefficients={"RHOB": -3.032, "U": 0.45, "DT": -0.01028},
        rms=53.9,
        reference="Fuchs et al. (2015), Table 3, A13",
    ),

    "A14": Equation(
        id="A14",
        property="tc",
        rock_group="evaporite",
        required_inputs=("PHIN", "U", "DT"),
        intercept=3.11,
        coefficients={"PHIN": -8.86, "U": 0.028, "DT": 0.00855},
        rms=22.6,
        reference="Fuchs et al. (2015), Table 3, A14",
    ),

    "A15": Equation(
        id="A15",
        property="tc",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=14.32,
        coefficients={"RHOB": -3.153, "PHIN": -8.93, "U": 0.005, "DT": -0.00631},
        rms=14.8,
        reference="Fuchs et al. (2015), Table 3, A15",
    ),
    
    #CARBONATE
    "A16": Equation(
        id="A16",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB",),
        intercept=-4.45,
        coefficients={"RHOB": 2.985},
        rms=17.9,
        reference="Fuchs et al. (2015), Table 3, A16",
    ),

    "A17": Equation(
        id="A17",
        property="tc",
        rock_group="carbonate",
        required_inputs=("PHIN",),
        intercept=3.92,
        coefficients={"PHIN": -5.11},
        rms=17.1,
        reference="Fuchs et al. (2015), Table 3, A17",
    ),

    "A18": Equation(
        id="A18",
        property="tc",
        rock_group="carbonate",
        required_inputs=("U",),
        intercept=1.76,
        coefficients={"U": 0.118},
        rms=26.0,
        reference="Fuchs et al. (2015), Table 3, A18",
    ),

    "A19": Equation(
        id="A19",
        property="tc",
        rock_group="carbonate",
        required_inputs=("DT",),
        intercept=5.56,
        coefficients={"DT": -0.012},
        rms=17.0,
        reference="Fuchs et al. (2015), Table 3, A19",
    ),

    "A20": Equation(
        id="A20",
        property="tc",
        rock_group="carbonate",
        required_inputs=("VSH",),
        intercept=3.60,
        coefficients={"VSH": -1.96},
        rms=20.7,
        reference="Fuchs et al. (2015), Table 3, A20",
    ),

    "A21": Equation(
        id="A21",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN"),
        intercept=0.08,
        coefficients={"RHOB": 1.411, "PHIN": -3.15},
        rms=16.2,
        reference="Fuchs et al. (2015), Table 3, A21",
    ),

    "A22": Equation(
        id="A22",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "U"),
        intercept=-6.45,
        coefficients={"RHOB": 4.648, "U": -0.27},
        rms=14.7,
        reference="Fuchs et al. (2015), Table 3, A22",
    ),

    "A23": Equation(
        id="A23",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "DT"),
        intercept=0.24,
        coefficients={"RHOB": 1.632, "DT": -0.006},
        rms=16.8,
        reference="Fuchs et al. (2015), Table 3, A23",
    ),

    "A24": Equation(
        id="A24",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "VSH"),
        intercept=-2.40,
        coefficients={"RHOB": 2.393, "VSH": -1.29},
        rms=14.3,
        reference="Fuchs et al. (2015), Table 3, A24",
    ),

    "A25": Equation(
        id="A25",
        property="tc",
        rock_group="carbonate",
        required_inputs=("PHIN", "U"),
        intercept=4.84,
        coefficients={"PHIN": -5.88, "U": -0.101},
        rms=17.0,
        reference="Fuchs et al. (2015), Table 3, A25",
    ),

    "A26": Equation(
        id="A26",
        property="tc",
        rock_group="carbonate",
        required_inputs=("PHIN", "DT"),
        intercept=4.43,
        coefficients={"PHIN": -3.78, "DT": -0.0034},
        rms=16.9,
        reference="Fuchs et al. (2015), Table 3, A26",
    ),

    "A27": Equation(
        id="A27",
        property="tc",
        rock_group="carbonate",
        required_inputs=("PHIN", "VSH"),
        intercept=4.24,
        coefficients={"PHIN": -4.08, "VSH": -1.17},
        rms=14.1,
        reference="Fuchs et al. (2015), Table 3, A27",
    ),

    "A28": Equation(
        id="A28",
        property="tc",
        rock_group="carbonate",
        required_inputs=("U", "DT"),
        intercept=7.02,
        coefficients={"U": -0.12, "DT": -0.01418},
        rms=17.1,
        reference="Fuchs et al. (2015), Table 3, A28",
    ),

    "A29": Equation(
        id="A29",
        property="tc",
        rock_group="carbonate",
        required_inputs=("U", "VSH"),
        intercept=3.39,
        coefficients={"U": 0.025, "VSH": -1.9},
        rms=20.6,
        reference="Fuchs et al. (2015), Table 3, A29",
    ),

    "A30": Equation(
        id="A30",
        property="tc",
        rock_group="carbonate",
        required_inputs=("DT", "VSH"),
        intercept=5.84,
        coefficients={"DT": -0.00997, "VSH": -1.48},
        rms=12.1,
        reference="Fuchs et al. (2015), Table 3, A30",
    ),

    "A31": Equation(
        id="A31",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=-2.80,
        coefficients={"RHOB": 3.301, "PHIN": -2.43, "U": -0.248},
        rms=13.6,
        reference="Fuchs et al. (2015), Table 3, A31",
    ),

    "A32": Equation(
        id="A32",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=-1.39,
        coefficients={"RHOB": 1.763, "PHIN": -4.01, "DT": 0.00344},
        rms=16.3,
        reference="Fuchs et al. (2015), Table 3, A32",
    ),

    "A33": Equation(
        id="A33",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "VSH"),
        intercept=0.59,
        coefficients={"RHOB": 1.34, "PHIN": -2.24, "VSH": -1.15},
        rms=13.2,
        reference="Fuchs et al. (2015), Table 3, A33",
    ),

    "A34": Equation(
        id="A34",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "DT"),
        intercept=-4.37,
        coefficients={"RHOB": 4.005, "U": -0.259, "DT": -0.00253},
        rms=14.5,
        reference="Fuchs et al. (2015), Table 3, A34",
    ),

    "A35": Equation(
        id="A35",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "VSH"),
        intercept=-4.37,
        coefficients={"RHOB": 4.178, "U": -0.302, "VSH": -1.45},
        rms=8.0,
        reference="Fuchs et al. (2015), Table 3, A35",
    ),

    "A36": Equation(
        id="A36",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "DT", "VSH"),
        intercept=5.01,
        coefficients={"RHOB": 0.254, "DT": -0.0091, "VSH": -1.45},
        rms=12.1,
        reference="Fuchs et al. (2015), Table 3, A36",
    ),

    "A37": Equation(
        id="A37",
        property="tc",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "DT"),
        intercept=5.88,
        coefficients={"PHIN": -3.74, "U": -0.119, "DT": -0.00582},
        rms=16.6,
        reference="Fuchs et al. (2015), Table 3, A37",
    ),

    "A38": Equation(
        id="A38",
        property="tc",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "VSH"),
        intercept=5.46,
        coefficients={"PHIN": -4.97, "U": -0.13, "VSH": -1.28},
        rms=13.4,
        reference="Fuchs et al. (2015), Table 3, A38",
    ),

    "A39": Equation(
        id="A39",
        property="tc",
        rock_group="carbonate",
        required_inputs=("PHIN", "DT", "VSH"),
        intercept=6.19,
        coefficients={"PHIN": 1.08, "DT": -0.01226, "VSH": -1.58},
        rms=12.0,
        reference="Fuchs et al. (2015), Table 3, A39",
    ),

    "A40": Equation(
        id="A40",
        property="tc",
        rock_group="carbonate",
        required_inputs=("U", "DT", "VSH"),
        intercept=8.24,
        coefficients={"U": -0.194, "DT": -0.01345, "VSH": -1.74},
        rms=9.8,
        reference="Fuchs et al. (2015), Table 3, A40",
    ),

    "A41": Equation(
        id="A41",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=-6.19,
        coefficients={"RHOB": 4.191, "PHIN": -4.25, "U": -0.264, "DT": 0.00749},
        rms=13.3,
        reference="Fuchs et al. (2015), Table 3, A41",
    ),

    "A42": Equation(
        id="A42",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "VSH"),
        intercept=-2.67,
        coefficients={"RHOB": 3.534, "PHIN": -1.21, "U": -0.29, "VSH": -1.37},
        rms=7.6,
        reference="Fuchs et al. (2015), Table 3, A42",
    ),

    "A43": Equation(
        id="A43",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "DT", "VSH"),
        intercept=5.77,
        coefficients={"RHOB": 0.119, "PHIN": 1.0, "DT": -0.01168, "VSH": -1.56},
        rms=12.0,
        reference="Fuchs et al. (2015), Table 3, A43",
    ),

    "A44": Equation(
        id="A44",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "DT", "VSH"),
        intercept=0.33,
        coefficients={"RHOB": 2.731, "U": -0.28, "DT": -0.00559, "VSH": -1.54},
        rms=7.0,
        reference="Fuchs et al. (2015), Table 3, A44",
    ),

    "A45": Equation(
        id="A45",
        property="tc",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "DT", "VSH"),
        intercept=9.12,
        coefficients={"PHIN": 2.36, "U": -0.204, "DT": -0.01863, "VSH": -1.97},
        rms=9.3,
        reference="Fuchs et al. (2015), Table 3, A45",
    ),

    "A46": Equation(
        id="A46",
        property="tc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "DT", "VSH"),
        intercept=1.15,
        coefficients={"RHOB": 2.587, "PHIN": 1.08, "U": -0.28, "DT": -0.00838, "VSH": -1.66},
        rms=6.9,
        reference="Fuchs et al. (2015), Table 3, A46",
    ),
# clastics 
    "A47": Equation(
        id="A47",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB",),
        intercept=-3.30,
        coefficients={"RHOB": 2.361},
        rms=22.0,
        reference="Fuchs et al. (2015), Table 3, A47",
    ),

    "A48": Equation(
        id="A48",
        property="tc",
        rock_group="clastic",
        required_inputs=("PHIN",),
        intercept=3.41,
        coefficients={"PHIN": -4.83},
        rms=19.0,
        reference="Fuchs et al. (2015), Table 3, A48",
    ),

    "A49": Equation(
        id="A49",
        property="tc",
        rock_group="clastic",
        required_inputs=("U",),
        intercept=2.14,
        coefficients={"U": 0.029},
        rms=28.1,
        reference="Fuchs et al. (2015), Table 3, A49",
    ),

    "A50": Equation(
        id="A50",
        property="tc",
        rock_group="clastic",
        required_inputs=("DT",),
        intercept=4.81,
        coefficients={"DT": -0.00974},
        rms=21.2,
        reference="Fuchs et al. (2015), Table 3, A50",
    ),

    "A51": Equation(
        id="A51",
        property="tc",
        rock_group="clastic",
        required_inputs=("VSH",),
        intercept=3.60,
        coefficients={"VSH": -2.31},
        rms=21.2,
        reference="Fuchs et al. (2015), Table 3, A51",
    ),

    "A52": Equation(
        id="A52",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN"),
        intercept=2.52,
        coefficients={"RHOB": 0.331, "PHIN": -4.38},
        rms=18.9,
        reference="Fuchs et al. (2015), Table 3, A52",
    ),

    "A53": Equation(
        id="A53",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "U"),
        intercept=-5.70,
        coefficients={"RHOB": 4.364, "U": -0.335},
        rms=17.3,
        reference="Fuchs et al. (2015), Table 3, A53",
    ),

    "A54": Equation(
        id="A54",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "DT"),
        intercept=1.14,
        coefficients={"RHOB": 1.117, "DT": -0.00578},
        rms=21.0,
        reference="Fuchs et al. (2015), Table 3, A54",
    ),

    "A55": Equation(
        id="A55",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "VSH"),
        intercept=-1.28,
        coefficients={"RHOB": 1.974, "VSH": -2.02},
        rms=15.9,
        reference="Fuchs et al. (2015), Table 3, A55",
    ),

    "A56": Equation(
        id="A56",
        property="tc",
        rock_group="clastic",
        required_inputs=("PHIN", "U"),
        intercept=4.03,
        coefficients={"PHIN": -5.17, "U": -0.077},
        rms=19.0,
        reference="Fuchs et al. (2015), Table 3, A56",
    ),

    "A57": Equation(
        id="A57",
        property="tc",
        rock_group="clastic",
        required_inputs=("PHIN", "DT"),
        intercept=1.01,
        coefficients={"PHIN": -10.87, "DT": 0.01474},
        rms=18.2,
        reference="Fuchs et al. (2015), Table 3, A57",
    ),

    "A58": Equation(
        id="A58",
        property="tc",
        rock_group="clastic",
        required_inputs=("PHIN", "VSH"),
        intercept=4.17,
        coefficients={"PHIN": -3.89, "VSH": -1.78},
        rms=14.1,
        reference="Fuchs et al. (2015), Table 3, A58",
    ),

    "A59": Equation(
        id="A59",
        property="tc",
        rock_group="clastic",
        required_inputs=("U", "DT"),
        intercept=6.20,
        coefficients={"U": -0.126, "DT": -0.0117},
        rms=20.7,
        reference="Fuchs et al. (2015), Table 3, A59",
    ),

    "A60": Equation(
        id="A60",
        property="tc",
        rock_group="clastic",
        required_inputs=("U", "VSH"),
        intercept=2.90,
        coefficients={"U": 0.115, "VSH": -2.52},
        rms=19.8,
        reference="Fuchs et al. (2015), Table 3, A60",
    ),

    "A61": Equation(
        id="A61",
        property="tc",
        rock_group="clastic",
        required_inputs=("DT", "VSH"),
        intercept=5.59,
        coefficients={"DT": -0.0084, "VSH": -2.05},
        rms=15.0,
        reference="Fuchs et al. (2015), Table 3, A61",
    ),

    "A62": Equation(
        id="A62",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=-3.87,
        coefficients={"RHOB": 3.577, "PHIN": -1.15, "U": -0.293},
        rms=17.1,
        reference="Fuchs et al. (2015), Table 3, A62",
    ),

    "A63": Equation(
        id="A63",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=-6.93,
        coefficients={"RHOB": 2.226, "PHIN": -12.64, "DT": 0.02662},
        rms=16.6,
        reference="Fuchs et al. (2015), Table 3, A63",
    ),

    "A64": Equation(
        id="A64",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "VSH"),
        intercept=2.54,
        coefficients={"RHOB": 0.609, "PHIN": -3.03, "VSH": -1.81},
        rms=13.8,
        reference="Fuchs et al. (2015), Table 3, A64",
    ),

    "A65": Equation(
        id="A65",
        property="tc",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "DT"),
        intercept=0.94,
        coefficients={"PHIN": -10.95, "U": 0.003, "DT": 0.01498},
        rms=18.1,
        reference="Fuchs et al. (2015), Table 3, A65",
    ),

    "A66": Equation(
        id="A66",
        property="tc",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "VSH"),
        intercept=4.08,
        coefficients={"PHIN": -3.82, "U": 0.013, "VSH": -1.81},
        rms=14.0,
        reference="Fuchs et al. (2015), Table 3, A66",
    ),

    "A67": Equation(
        id="A67",
        property="tc",
        rock_group="clastic",
        required_inputs=("PHIN", "DT", "VSH"),
        intercept=3.66,
        coefficients={"PHIN": -5.13, "DT": 0.00293, "VSH": -1.7},
        rms=14.0,
        reference="Fuchs et al. (2015), Table 3, A67",
    ),

    "A68": Equation(
        id="A68",
        property="tc",
        rock_group="clastic",
        required_inputs=("U", "DT", "VSH"),
        intercept=5.76,
        coefficients={"U": -0.018, "DT": -0.0087, "VSH": -2.01},
        rms=15.0,
        reference="Fuchs et al. (2015), Table 3, A68",
    ),

    "A69": Equation(
        id="A69",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "DT", "VSH"),
        intercept=3.34,
        coefficients={"RHOB": 0.681, "DT": -0.006, "VSH": -2.03},
        rms=14.8,
        reference="Fuchs et al. (2015), Table 3, A69",
    ),

    "A70": Equation(
        id="A70",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "DT"),
        intercept=-7.95,
        coefficients={"RHOB": 5.097, "U": -0.36, "DT": 0.0027},
        rms=17.3,
        reference="Fuchs et al. (2015), Table 3, A70",
    ),

    "A71": Equation(
        id="A71",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "VSH"),
        intercept=-3.14,
        coefficients={"RHOB": 3.187, "U": -0.186, "VSH": -1.49},
        rms=14.3,
        reference="Fuchs et al. (2015), Table 3, A71",
    ),

    "A72": Equation(
        id="A72",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=-10.01,
        coefficients={"RHOB": 4.361, "PHIN": -8.55, "U": -0.226, "DT": 0.02145},
        rms=15.3,
        reference="Fuchs et al. (2015), Table 3, A72",
    ),

    "A73": Equation(
        id="A73",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "VSH"),
        intercept=0.36,
        coefficients={"RHOB": 1.685, "PHIN": -2.09, "U": -0.1, "VSH": -1.59},
        rms=13.6,
        reference="Fuchs et al. (2015), Table 3, A73",
    ),

    "A74": Equation(
        id="A74",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "DT", "VSH"),
        intercept=-1.55,
        coefficients={"RHOB": 1.386, "PHIN": -6.81, "DT": 0.01152, "VSH": -1.53},
        rms=13.2,
        reference="Fuchs et al. (2015), Table 3, A74",
    ),

    "A75": Equation(
        id="A75",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "DT", "VSH"),
        intercept=-1.06,
        coefficients={"RHOB": 2.491, "U": -0.155, "DT": -0.0023, "VSH": -1.58},
        rms=14.02,
        reference="Fuchs et al. (2015), Table 3, A75",
    ),

    "A76": Equation(
        id="A76",
        property="tc",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "DT", "VSH"),
        intercept=2.94,
        coefficients={"PHIN": -6.0, "U": 0.038, "DT": 0.00551, "VSH": -1.73},
        rms=13.8,
        reference="Fuchs et al. (2015), Table 3, A76",
    ),

    "A77": Equation(
        id="A77",
        property="tc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "DT", "VSH"),
        intercept=-3.60,
        coefficients={"RHOB": 2.416, "PHIN": -5.84, "U": -0.097, "DT": 0.01133, "VSH": -1.32},
        rms=13.0,
        reference="Fuchs et al. (2015), Table 3, A77",
    ),
    # TD
    # evaporites
    "B1": Equation(
        id="B1",
        property="td",
        rock_group="evaporite",
        required_inputs=("RHOB",),
        intercept=2.09,
        coefficients={"RHOB": -0.27},
        rms=92.0,
        reference="Fuchs et al. (2015), Table 3, B1",
    ),

    "B2": Equation(
        id="B2",
        property="td",
        rock_group="evaporite",
        required_inputs=("PHIN",),
        intercept=2.49,
        coefficients={"PHIN": -4.35},
        rms=37.5,
        reference="Fuchs et al. (2015), Table 3, B2",
    ),

    "B3": Equation(
        id="B3",
        property="td",
        rock_group="evaporite",
        required_inputs=("U",),
        intercept=-1.25,
        coefficients={"U": 0.27},
        rms=54.0,
        reference="Fuchs et al. (2015), Table 3, B3",
    ),

    "B4": Equation(
        id="B4",
        property="td",
        rock_group="evaporite",
        required_inputs=("DT",),
        intercept=1.91,
        coefficients={"DT": -0.0018},
        rms=87.2,
        reference="Fuchs et al. (2015), Table 3, B4",
    ),

    "B5": Equation(
        id="B5",
        property="td",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN"),
        intercept=4.94,
        coefficients={"RHOB": -1.01, "PHIN": -4.84},
        rms=31.9,
        reference="Fuchs et al. (2015), Table 3, B5",
    ),

    "B6": Equation(
        id="B6",
        property="td",
        rock_group="evaporite",
        required_inputs=("RHOB", "U"),
        intercept=0.14,
        coefficients={"RHOB": -0.69, "U": 0.29},
        rms=56.0,
        reference="Fuchs et al. (2015), Table 3, B6",
    ),

    "B7": Equation(
        id="B7",
        property="td",
        rock_group="evaporite",
        required_inputs=("RHOB", "DT"),
        intercept=8.50,
        coefficients={"RHOB": -1.9, "DT": -0.01065},
        rms=99.2,
        reference="Fuchs et al. (2015), Table 3, B7",
    ),

    "B8": Equation(
        id="B8",
        property="td",
        rock_group="evaporite",
        required_inputs=("PHIN", "U"),
        intercept=1.70,
        coefficients={"PHIN": -3.83, "U": 0.07},
        rms=36.7,
        reference="Fuchs et al. (2015), Table 3, B8",
    ),

    "B9": Equation(
        id="B9",
        property="td",
        rock_group="evaporite",
        required_inputs=("PHIN", "DT"),
        intercept=1.78,
        coefficients={"PHIN": -4.71, "DT": 0.00321},
        rms=39.3,
        reference="Fuchs et al. (2015), Table 3, B9",
    ),

    "B10": Equation(
        id="B10",
        property="td",
        rock_group="evaporite",
        required_inputs=("U", "DT"),
        intercept=-1.69,
        coefficients={"U": 0.28, "DT": 0.00135},
        rms=53.5,
        reference="Fuchs et al. (2015), Table 3, B10",
    ),

    "B11": Equation(
        id="B11",
        property="td",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=4.10,
        coefficients={"RHOB": -1.03, "PHIN": -4.26, "U": 0.07},
        rms=30.4,
        reference="Fuchs et al. (2015), Table 3, B11",
    ),

    "B12": Equation(
        id="B12",
        property="td",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=7.83,
        coefficients={"RHOB": -1.75, "PHIN": -4.65, "DT": -0.00499},
        rms=27.6,
        reference="Fuchs et al. (2015), Table 3, B12",
    ),

    "B13": Equation(
        id="B13",
        property="td",
        rock_group="evaporite",
        required_inputs=("RHOB", "U", "DT"),
        intercept=4.14,
        coefficients={"RHOB": -1.65, "U": 0.27, "DT": -0.00642},
        rms=63.0,
        reference="Fuchs et al. (2015), Table 3, B13",
    ),

    "B14": Equation(
        id="B14",
        property="td",
        rock_group="evaporite",
        required_inputs=("PHIN", "U", "DT"),
        intercept=0.80,
        coefficients={"PHIN": -4.12, "U": 0.08, "DT": 0.00345},
        rms=37.8,
        reference="Fuchs et al. (2015), Table 3, B14",
    ),

    "B15": Equation(
        id="B15",
        property="td",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=6.86,
        coefficients={"RHOB": -1.7, "PHIN": -4.16, "U": 0.06, "DT": -0.00457},
        rms=27.2,
        reference="Fuchs et al. (2015), Table 3, B15",
    ),
# carbonates
    "B16": Equation(
        id="B16",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB",),
        intercept=-2.67,
        coefficients={"RHOB": 1.58},
        rms=20.9,
        reference="Fuchs et al. (2015), Table 3, B16",
    ),

    "B17": Equation(
        id="B17",
        property="td",
        rock_group="carbonate",
        required_inputs=("PHIN",),
        intercept=1.83,
        coefficients={"PHIN": -2.95},
        rms=15.5,
        reference="Fuchs et al. (2015), Table 3, B17",
    ),

    "B18": Equation(
        id="B18",
        property="td",
        rock_group="carbonate",
        required_inputs=("U",),
        intercept=0.57,
        coefficients={"U": 0.07},
        rms=33.3,
        reference="Fuchs et al. (2015), Table 3, B18",
    ),

    "B19": Equation(
        id="B19",
        property="td",
        rock_group="carbonate",
        required_inputs=("DT",),
        intercept=2.79,
        coefficients={"DT": -0.00687},
        rms=15.5,
        reference="Fuchs et al. (2015), Table 3, B19",
    ),

    "B20": Equation(
        id="B20",
        property="td",
        rock_group="carbonate",
        required_inputs=("VSH",),
        intercept=1.45,
        coefficients={"VSH": -0.75},
        rms=31.0,
        reference="Fuchs et al. (2015), Table 3, B20",
    ),

    "B21": Equation(
        id="B21",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN"),
        intercept=0.86,
        coefficients={"RHOB": 0.36, "PHIN": -2.46},
        rms=15.1,
        reference="Fuchs et al. (2015), Table 3, B21",
    ),

    "B22": Equation(
        id="B22",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "U"),
        intercept=-3.61,
        coefficients={"RHOB": 2.37, "U": -0.13},
        rms=16.7,
        reference="Fuchs et al. (2015), Table 3, B22",
    ),

    "B23": Equation(
        id="B23",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "DT"),
        intercept=2.41,
        coefficients={"RHOB": 0.12, "DT": -0.00645},
        rms=15.6,
        reference="Fuchs et al. (2015), Table 3, B23",
    ),

    "B24": Equation(
        id="B24",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "VSH"),
        intercept=-2.11,
        coefficients={"RHOB": 1.42, "VSH": -0.35},
        rms=19.7,
        reference="Fuchs et al. (2015), Table 3, B24",
    ),

    "B25": Equation(
        id="B25",
        property="td",
        rock_group="carbonate",
        required_inputs=("PHIN", "U"),
        intercept=2.34,
        coefficients={"PHIN": -3.37, "U": -0.06},
        rms=14.7,
        reference="Fuchs et al. (2015), Table 3, B25",
    ),

    "B26": Equation(
        id="B26",
        property="td",
        rock_group="carbonate",
        required_inputs=("PHIN", "DT"),
        intercept=2.19,
        coefficients={"PHIN": -2.01, "DT": -0.00239},
        rms=14.6,
        reference="Fuchs et al. (2015), Table 3, B26",
    ),

    "B27": Equation(
        id="B27",
        property="td",
        rock_group="carbonate",
        required_inputs=("PHIN", "VSH"),
        intercept=1.89,
        coefficients={"PHIN": -2.76, "VSH": -0.21},
        rms=15.1,
        reference="Fuchs et al. (2015), Table 3, B27",
    ),

    "B28": Equation(
        id="B28",
        property="td",
        rock_group="carbonate",
        required_inputs=("U", "DT"),
        intercept=3.62,
        coefficients={"U": -0.07, "DT": -0.00821},
        rms=14.3,
        reference="Fuchs et al. (2015), Table 3, B28",
    ),

    "B29": Equation(
        id="B29",
        property="td",
        rock_group="carbonate",
        required_inputs=("U", "VSH"),
        intercept=1.14,
        coefficients={"U": 0.04, "VSH": -0.67},
        rms=30.1,
        reference="Fuchs et al. (2015), Table 3, B29",
    ),

    "B30": Equation(
        id="B30",
        property="td",
        rock_group="carbonate",
        required_inputs=("DT", "VSH"),
        intercept=2.88,
        coefficients={"DT": -0.00632, "VSH": -0.44},
        rms=13.4,
        reference="Fuchs et al. (2015), Table 3, B30",
    ),

    "B31": Equation(
        id="B31",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=-0.39,
        coefficients={"RHOB": 1.18, "PHIN": -2.14, "U": -0.11},
        rms=11.6,
        reference="Fuchs et al. (2015), Table 3, B31",
    ),

    "B32": Equation(
        id="B32",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=1.58,
        coefficients={"RHOB": 0.18, "PHIN": -2.04, "DT": -0.00168},
        rms=14.7,
        reference="Fuchs et al. (2015), Table 3, B32",
    ),

    "B33": Equation(
        id="B33",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "VSH"),
        intercept=0.96,
        coefficients={"RHOB": 0.34, "PHIN": -2.29, "VSH": -0.21},
        rms=14.7,
        reference="Fuchs et al. (2015), Table 3, B33",
    ),

    "B34": Equation(
        id="B34",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "DT"),
        intercept=0.53,
        coefficients={"RHOB": 1.09, "U": -0.11, "DT": -0.00505},
        rms=13.3,
        reference="Fuchs et al. (2015), Table 3, B34",
    ),

    "B35": Equation(
        id="B35",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "VSH"),
        intercept=-3.00,
        coefficients={"RHOB": 2.23, "U": -0.14, "VSH": -0.43},
        rms=14.2,
        reference="Fuchs et al. (2015), Table 3, B35",
    ),

    "B36": Equation(
        id="B36",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "DT", "VSH"),
        intercept=4.01,
        coefficients={"RHOB": -0.34, "DT": -0.0075, "VSH": -0.48},
        rms=13.2,
        reference="Fuchs et al. (2015), Table 3, B36",
    ),

    "B37": Equation(
        id="B37",
        property="td",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "DT"),
        intercept=3.01,
        coefficients={"PHIN": -1.99, "U": -0.07, "DT": -0.00376},
        rms=13.3,
        reference="Fuchs et al. (2015), Table 3, B37",
    ),

    "B38": Equation(
        id="B38",
        property="td",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "VSH"),
        intercept=2.47,
        coefficients={"PHIN": -3.18, "U": -0.06, "VSH": -0.27},
        rms=14.0,
        reference="Fuchs et al. (2015), Table 3, B38",
    ),

    "B39": Equation(
        id="B39",
        property="td",
        rock_group="carbonate",
        required_inputs=("PHIN", "DT", "VSH"),
        intercept=2.59,
        coefficients={"PHIN": -0.90, "DT": -0.00442, "VSH": -0.36},
        rms=13.3,
        reference="Fuchs et al. (2015), Table 3, B39",
    ),

    "B40": Equation(
        id="B40",
        property="td",
        rock_group="carbonate",
        required_inputs=("U", "DT", "VSH"),
        intercept=4.02,
        coefficients={"U": -0.09, "DT": -0.00797, "VSH": -0.57},
        rms=10.5,
        reference="Fuchs et al. (2015), Table 3, B40",
    ),

    "B41": Equation(
        id="B41",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=-0.39,
        coefficients={"RHOB": 1.18, "PHIN": -2.13, "U": -0.11, "DT": -2e-05},
        rms=11.6,
        reference="Fuchs et al. (2015), Table 3, B41",
    ),

    "B42": Equation(
        id="B42",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "VSH"),
        intercept=-0.37,
        coefficients={"RHOB": 1.23, "PHIN": -1.87, "U": -0.12, "VSH": -0.3},
        rms=10.3,
        reference="Fuchs et al. (2015), Table 3, B42",
    ),

    "B43": Equation(
        id="B43",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "DT", "VSH"),
        intercept=3.45,
        coefficients={"RHOB": -0.24, "PHIN": -0.73, "DT": -0.00561, "VSH": -0.41},
        rms=13.02,
        reference="Fuchs et al. (2015), Table 3, B43",
    ),

    "B44": Equation(
        id="B44",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "DT", "VSH"),
        intercept=2.12,
        coefficients={"RHOB": 0.65, "U": -0.11, "DT": -0.00609, "VSH": -0.52},
        rms=9.6,
        reference="Fuchs et al. (2015), Table 3, B44",
    ),

    "B45": Equation(
        id="B45",
        property="td",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "DT", "VSH"),
        intercept=3.89,
        coefficients={"PHIN": -0.33, "U": -0.09, "DT": -0.00725, "VSH": -0.54},
        rms=10.05,
        reference="Fuchs et al. (2015), Table 3, B45",
    ),

    "B46": Equation(
        id="B46",
        property="td",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "DT", "VSH"),
        intercept=1.59,
        coefficients={"RHOB": 0.75, "PHIN": -0.70, "U": -0.11, "DT": -0.00429, "VSH": -0.45},
        rms=9.4,
        reference="Fuchs et al. (2015), Table 3, B46",
    ),
# clastic
    "B47": Equation(
        id="B47",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB",),
        intercept=-2.42,
        coefficients={"RHOB": 1.44},
        rms=28.0,
        reference="Fuchs et al. (2015), Table 3, B47",
    ),

    "B48": Equation(
        id="B48",
        property="td",
        rock_group="clastic",
        required_inputs=("PHIN",),
        intercept=1.69,
        coefficients={"PHIN": -3.09},
        rms=19.4,
        reference="Fuchs et al. (2015), Table 3, B48",
    ),

    "B49": Equation(
        id="B49",
        property="td",
        rock_group="clastic",
        required_inputs=("U",),
        intercept=0.84,
        coefficients={"U": 0.02},
        rms=39.2,
        reference="Fuchs et al. (2015), Table 3, B49",
    ),

    "B50": Equation(
        id="B50",
        property="td",
        rock_group="clastic",
        required_inputs=("DT",),
        intercept=2.68,
        coefficients={"DT": -0.00659},
        rms=22.6,
        reference="Fuchs et al. (2015), Table 3, B50",
    ),

    "B51": Equation(
        id="B51",
        property="td",
        rock_group="clastic",
        required_inputs=("VSH",),
        intercept=1.54,
        coefficients={"VSH": -0.97},
        rms=33.8,
        reference="Fuchs et al. (2015), Table 3, B51",
    ),

    "B52": Equation(
        id="B52",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN"),
        intercept=1.66,
        coefficients={"RHOB": 0.01, "PHIN": -3.07},
        rms=19.4,
        reference="Fuchs et al. (2015), Table 3, B52",
    ),

    "B53": Equation(
        id="B53",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "U"),
        intercept=-3.79,
        coefficients={"RHOB": 2.58, "U": -0.19},
        rms=19.8,
        reference="Fuchs et al. (2015), Table 3, B53",
    ),

    "B54": Equation(
        id="B54",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "DT"),
        intercept=2.43,
        coefficients={"RHOB": 0.08, "DT": -0.00633},
        rms=22.6,
        reference="Fuchs et al. (2015), Table 3, B54",
    ),

    "B55": Equation(
        id="B55",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "VSH"),
        intercept=-1.64,
        coefficients={"RHOB": 1.29, "VSH": -0.78},
        rms=24.2,
        reference="Fuchs et al. (2015), Table 3, B55",
    ),

    "B56": Equation(
        id="B56",
        property="td",
        rock_group="clastic",
        required_inputs=("PHIN", "U"),
        intercept=2.04,
        coefficients={"PHIN": -3.28, "U": -0.04},
        rms=19.0,
        reference="Fuchs et al. (2015), Table 3, B56",
    ),

    "B57": Equation(
        id="B57",
        property="td",
        rock_group="clastic",
        required_inputs=("PHIN", "DT"),
        intercept=0.94,
        coefficients={"PHIN": -4.99, "DT": 0.00465},
        rms=19.0,
        reference="Fuchs et al. (2015), Table 3, B57",
    ),

    "B58": Equation(
        id="B58",
        property="td",
        rock_group="clastic",
        required_inputs=("PHIN", "VSH"),
        intercept=1.95,
        coefficients={"PHIN": -2.77, "VSH": -0.6},
        rms=17.7,
        reference="Fuchs et al. (2015), Table 3, B58",
    ),

    "B59": Equation(
        id="B59",
        property="td",
        rock_group="clastic",
        required_inputs=("U", "DT"),
        intercept=3.56,
        coefficients={"U": -0.08, "DT": -0.00783},
        rms=20.9,
        reference="Fuchs et al. (2015), Table 3, B59",
    ),

    "B60": Equation(
        id="B60",
        property="td",
        rock_group="clastic",
        required_inputs=("U", "VSH"),
        intercept=1.17,
        coefficients={"U": 0.06, "VSH": -1.09},
        rms=32.2,
        reference="Fuchs et al. (2015), Table 3, B60",
    ),

    "B61": Equation(
        id="B61",
        property="td",
        rock_group="clastic",
        required_inputs=("DT", "VSH"),
        intercept=2.98,
        coefficients={"DT": -0.00608, "VSH": -0.79},
        rms=19.3,
        reference="Fuchs et al. (2015), Table 3, B61",
    ),

    "B62": Equation(
        id="B62",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=-1.21,
        coefficients={"RHOB": 1.48, "PHIN": -1.62, "U": -0.13},
        rms=17.8,
        reference="Fuchs et al. (2015), Table 3, B62",
    ),

    "B63": Equation(
        id="B63",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=-1.03,
        coefficients={"RHOB": 0.55, "PHIN": -5.43, "DT": 0.0076},
        rms=18.7,
        reference="Fuchs et al. (2015), Table 3, B63",
    ),

    "B64": Equation(
        id="B64",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "VSH"),
        intercept=1.67,
        coefficients={"RHOB": 0.1, "PHIN": -2.63, "VSH": -0.6},
        rms=17.7,
        reference="Fuchs et al. (2015), Table 3, B64",
    ),

    "B65": Equation(
        id="B65",
        property="td",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "DT"),
        intercept=1.53,
        coefficients={"PHIN": -4.23, "U": -0.03, "DT": 0.00248},
        rms=18.9,
        reference="Fuchs et al. (2015), Table 3, B65",
    ),

    "B66": Equation(
        id="B66",
        property="td",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "VSH"),
        intercept=2.06,
        coefficients={"PHIN": -2.86, "U": -0.02, "VSH": -0.55},
        rms=17.6,
        reference="Fuchs et al. (2015), Table 3, B66",
    ),

    "B67": Equation(
        id="B67",
        property="td",
        rock_group="clastic",
        required_inputs=("PHIN", "DT", "VSH"),
        intercept=1.84,
        coefficients={"PHIN": -3.04, "DT": 0.00064, "VSH": -0.58},
        rms=17.7,
        reference="Fuchs et al. (2015), Table 3, B67",
    ),

    "B68": Equation(
        id="B68",
        property="td",
        rock_group="clastic",
        required_inputs=("U", "DT", "VSH"),
        intercept=3.41,
        coefficients={"U": -0.04, "DT": -0.00681, "VSH": -0.69},
        rms=18.7,
        reference="Fuchs et al. (2015), Table 3, B68",
    ),

    "B69": Equation(
        id="B69",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "DT", "VSH"),
        intercept=3.29,
        coefficients={"RHOB": -0.09, "DT": -0.00641, "VSH": -0.79},
        rms=19.3,
        reference="Fuchs et al. (2015), Table 3, B69",
    ),

    "B70": Equation(
        id="B70",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "DT"),
        intercept=-1.82,
        coefficients={"RHOB": 1.94, "U": -0.17, "DT": -0.00236},
        rms=18.9,
        reference="Fuchs et al. (2015), Table 3, B70",
    ),

    "B71": Equation(
        id="B71",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "DT", "VSH"),
        intercept=-3.21,
        coefficients={"RHOB": 2.31, "U": -0.16, "DT": 0.00493, "VSH": -0.34},
        rms=19.4,
        reference="Fuchs et al. (2015), Table 3, B71",
    ),

    "B72": Equation(
        id="B72",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=-2.62,
        coefficients={"RHOB": 1.65, "PHIN": -3.32, "U": -0.12, "DT": 0.00493},
        rms=17.3,
        reference="Fuchs et al. (2015), Table 3, B72",
    ),

    "B73": Equation(
        id="B73",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "VSH"),
        intercept=-0.08,
        coefficients={"RHOB": 0.97, "PHIN": -1.87, "U": -0.08, "VSH": -0.43},
        rms=17.0,
        reference="Fuchs et al. (2015), Table 3, B73",
    ),

    "B74": Equation(
        id="B74",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "DT", "VSH"),
        intercept=0.89,
        coefficients={"RHOB": 0.25, "PHIN": -3.35, "DT": 0.0022, "VSH": -0.55},
        rms=17.6,
        reference="Fuchs et al. (2015), Table 3, B74",
    ),

    "B75": Equation(
        id="B75",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "DT", "VSH"),
        intercept=0.31,
        coefficients={"RHOB": 1.13, "U": -0.11, "DT": -0.00391, "VSH": -0.49},
        rms=17.9,
        reference="Fuchs et al. (2015), Table 3, B75",
    ),

    "B76": Equation(
        id="B76",
        property="td",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "DT", "VSH"),
        intercept=2.18,
        coefficients={"PHIN": -2.62, "U": -0.02, "DT": -0.0006, "VSH": -0.56},
        rms=17.7,
        reference="Fuchs et al. (2015), Table 3, B76",
    ),

    "B77": Equation(
        id="B77",
        property="td",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "DT", "VSH"),
        intercept=-0.79,
        coefficients={"RHOB": 1.1, "PHIN": -2.55, "U": -0.08, "DT": 0.00205, "VSH": -0.38},
        rms=16.9,
        reference="Fuchs et al. (2015), Table 3, B77",
    ),
#  SHC
    "C1": Equation(
        id="C1",
        property="shc",
        rock_group="evaporite",
        required_inputs=("RHOB",),
        intercept=2973.7,
        coefficients={"RHOB": -708.2},
        rms=22.2,
        reference="Fuchs et al. (2015), Table 3, C1",
    ),

    "C2": Equation(
        id="C2",
        property="shc",
        rock_group="evaporite",
        required_inputs=("PHIN",),
        intercept=1012.5,
        coefficients={"PHIN": 1382.1},
        rms=20.7,
        reference="Fuchs et al. (2015), Table 3, C2",
    ),

    "C3": Equation(
        id="C3",
        property="shc",
        rock_group="evaporite",
        required_inputs=("U",),
        intercept=2412.5,
        coefficients={"U": -107.9},
        rms=21.4,
        reference="Fuchs et al. (2015), Table 3, C3",
    ),

    "C4": Equation(
        id="C4",
        property="shc",
        rock_group="evaporite",
        required_inputs=("DT",),
        intercept=54.1,
        rms=16.2,
        coefficients={"DT": 5.188},

        reference="Fuchs et al. (2015), Table 3, C4",
    ),

    "C5": Equation(
        id="C5",
        property="shc",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN"),
        intercept=2312.9,
        coefficients={"RHOB": -535.9, "PHIN": 1123.3},
        rms=15.3,
        reference="Fuchs et al. (2015), Table 3, C5",
    ),

    "C6": Equation(
        id="C6",
        property="shc",
        rock_group="evaporite",
        required_inputs=("RHOB", "U"),
        intercept=3573.6,
        coefficients={"RHOB": -578.7, "U": -90.0},
        rms=15.8,
        reference="Fuchs et al. (2015), Table 3, C6",
    ),

    "C7": Equation(
        id="C7",
        property="shc",
        rock_group="evaporite",
        required_inputs=("RHOB", "DT"),
        intercept=-1002.1,
        coefficients={"RHOB": 305.0, "DT": 6.607},
        rms=16.1,
        reference="Fuchs et al. (2015), Table 3, C7",
    ),

    "C8": Equation(
        id="C8",
        property="shc",
        rock_group="evaporite",
        required_inputs=("PHIN", "U"),
        intercept=1703.6,
        coefficients={"PHIN": 920.9, "U": -58.4},
        rms=18.7,
        reference="Fuchs et al. (2015), Table 3, C8",
    ),

    "C9": Equation(
        id="C9",
        property="shc",
        rock_group="evaporite",
        required_inputs=("PHIN", "DT"),
        intercept=80.7,
        coefficients={"PHIN": 917.9, "DT": 4.213},
        rms=10.2,
        reference="Fuchs et al. (2015), Table 3, C9",
    ),

    "C10": Equation(
        id="C10",
        property="shc",
        rock_group="evaporite",
        required_inputs=("U", "DT"),
        intercept=991.1,
        coefficients={"U": -73.5, "DT": 4.369},
        rms=9.9,
        reference="Fuchs et al. (2015), Table 3, C10",
    ),

    "C11": Equation(
        id="C11",
        property="shc",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=2919.7,
        coefficients={"RHOB": -522.6, "PHIN": 703.4, "U": -54.0},
        rms=13.6,
        reference="Fuchs et al. (2015), Table 3, C11",
    ),

    "C12": Equation(
        id="C12",
        property="shc",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=-871.1,
        coefficients={"RHOB": 274.8, "PHIN": 908.6, "DT": 5.502},
        rms=10.0,
        reference="Fuchs et al. (2015), Table 3, C12",
    ),

    "C13": Equation(
        id="C13",
        property="shc",
        rock_group="evaporite",
        required_inputs=("RHOB", "U", "DT"),
        intercept=150.5,
        coefficients={"RHOB": 237.2, "U": -72.0, "DT": 5.49},
        rms=9.5,
        reference="Fuchs et al. (2015), Table 3, C13",
    ),

    "C14": Equation(
        id="C14",
        property="shc",
        rock_group="evaporite",
        required_inputs=("PHIN", "U", "DT"),
        intercept=640.4,
        coefficients={"PHIN": 580.3, "U": -44.7, "DT": 4.074},
        rms=7.8,
        reference="Fuchs et al. (2015), Table 3, C14",
    ),

    "C15": Equation(
        id="C15",
        property="shc",
        rock_group="evaporite",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=-231.7,
        coefficients={"RHOB": 245.2, "PHIN": 585.8, "U": -42.9, "DT": 5.23},
        rms=7.4,
        reference="Fuchs et al. (2015), Table 3, C15",
    ),
# carbonate
    "C16": Equation(
        id="C16",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB",),
        intercept=4771.7,
        coefficients={"RHOB": -1463.9},
        rms=16.8,
        reference="Fuchs et al. (2015), Table 3, C16",
    ),

    "C17": Equation(
        id="C17",
        property="shc",
        rock_group="carbonate",
        required_inputs=("PHIN",),
        intercept=636.6,
        coefficients={"PHIN": 2625.3},
        rms=12.4,
        reference="Fuchs et al. (2015), Table 3, C17",
    ),

    "C18": Equation(
        id="C18",
        property="shc",
        rock_group="carbonate",
        required_inputs=("U",),
        intercept=2014.5,
        coefficients={"U": -98.3},
        rms=24.9,
        reference="Fuchs et al. (2015), Table 3, C18",
    ),

    "C19": Equation(
        id="C19",
        property="shc",
        rock_group="carbonate",
        required_inputs=("DT",),
        intercept=-376.7,
        coefficients={"DT": 6.747},
        rms=7.8,
        reference="Fuchs et al. (2015), Table 3, C19",
    ),

    "C20": Equation(
        id="C20",
        property="shc",
        rock_group="carbonate",
        required_inputs=("VSH",),
        intercept=1292.8,
        coefficients={"VSH": 30.9},
        rms=28.5,
        reference="Fuchs et al. (2015), Table 3, C20",
    ),

    "C21": Equation(
        id="C21",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN"),
        intercept=1987.1,
        coefficients={"RHOB": -496.4, "PHIN": 1937.1},
        rms=11.7,
        reference="Fuchs et al. (2015), Table 3, C21",
    ),

    "C22": Equation(
        id="C22",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "U"),
        intercept=5138.0,
        coefficients={"RHOB": -1769.2, "U": 49.6},
        rms=14.8,
        reference="Fuchs et al. (2015), Table 3, C22",
    ),

    "C23": Equation(
        id="C23",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "DT"),
        intercept=-1555.4,
        coefficients={"RHOB": 361.4, "DT": 8.044},
        rms=7.4,
        reference="Fuchs et al. (2015), Table 3, C23",
    ),

    "C24": Equation(
        id="C24",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "VSH"),
        intercept=5466.7,
        coefficients={"RHOB": -1664.8, "VSH": -436.5},
        rms=13.4,
        reference="Fuchs et al. (2015), Table 3, C24",
    ),

    "C25": Equation(
        id="C25",
        property="shc",
        rock_group="carbonate",
        required_inputs=("PHIN", "U"),
        intercept=639.9,
        coefficients={"PHIN": 2622.5, "U": -0.4},
        rms=12.4,
        reference="Fuchs et al. (2015), Table 3, C25",
    ),

    "C26": Equation(
        id="C26",
        property="shc",
        rock_group="carbonate",
        required_inputs=("PHIN", "DT"),
        intercept=-411.5,
        coefficients={"PHIN": -115.6, "DT": 7.005},
        rms=7.8,
        reference="Fuchs et al. (2015), Table 3, C26",
    ),

    "C27": Equation(
        id="C27",
        property="shc",
        rock_group="carbonate",
        required_inputs=("PHIN", "VSH"),
        intercept=796.8,
        coefficients={"PHIN": 3136.0, "VSH": -578.1},
        rms=6.5,
        reference="Fuchs et al. (2015), Table 3, C27",
    ),

    "C28": Equation(
        id="C28",
        property="shc",
        rock_group="carbonate",
        required_inputs=("U", "DT"),
        intercept=-654.7,
        coefficients={"U": 23.0, "DT": 7.199},
        rms=7.3,
        reference="Fuchs et al. (2015), Table 3, C28",
    ),

    "C29": Equation(
        id="C29",
        property="shc",
        rock_group="carbonate",
        required_inputs=("U", "VSH"),
        intercept=2194.5,
        coefficients={"U": -108.6, "VSH": -210.0},
        rms=24.5,
        reference="Fuchs et al. (2015), Table 3, C29",
    ),

    "C30": Equation(
        id="C30",
        property="shc",
        rock_group="carbonate",
        required_inputs=("DT", "VSH"),
        intercept=-316.7,
        coefficients={"DT": 7.138, "VSH": -312.8},
        rms=4.7,
        reference="Fuchs et al. (2015), Table 3, C30",
    ),

    "C31": Equation(
        id="C31",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=2368.4,
        coefficients={"RHOB": -747.0, "PHIN": 1840.8, "U": 32.9},
        rms=11.2,
        reference="Fuchs et al. (2015), Table 3, C31",
    ),

    "C32": Equation(
        id="C32",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=-1622.0,
        coefficients={"RHOB": 366.7, "PHIN": -163.7, "DT": 8.427},
        rms=7.4,
        reference="Fuchs et al. (2015), Table 3, C32",
    ),

    "C33": Equation(
        id="C33",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "VSH"),
        intercept=2247.4,
        coefficients={"RHOB": -532.4, "PHIN": 2404.4, "VSH": -585.5},
        rms=4.6,
        reference="Fuchs et al. (2015), Table 3, C33",
    ),

    "C34": Equation(
        id="C34",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "DT"),
        intercept=-1281.5,
        coefficients={"RHOB": 220.4, "U": 15.4, "DT": 7.84},
        rms=7.2,
        reference="Fuchs et al. (2015), Table 3, C34",
    ),

    "C35": Equation(
        id="C35",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "VSH"),
        intercept=5728.7,
        coefficients={"RHOB": -1902.7, "U": 40.3, "VSH": -413.9},
        rms=12.4,
        reference="Fuchs et al. (2015), Table 3, C35",
    ),

    "C36": Equation(
        id="C36",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "DT", "VSH"),
        intercept=-551.7,
        coefficients={"RHOB": 71.6, "DT": 7.384, "VSH": -304.6},
        rms=4.6,
        reference="Fuchs et al. (2015), Table 3, C36",
    ),

    "C37": Equation(
        id="C37",
        property="shc",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "DT"),
        intercept=-692.0,
        coefficients={"PHIN": -122.8, "U": 23.0, "DT": 7.473},
        rms=7.3,
        reference="Fuchs et al. (2015), Table 3, C37",
    ),

    "C38": Equation(
        id="C38",
        property="shc",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "VSH"),
        intercept=926.7,
        coefficients={"PHIN": 3041.1, "U": -13.8, "VSH": -590.3},
        rms=6.3,
        reference="Fuchs et al. (2015), Table 3, C38",
    ),

    "C39": Equation(
        id="C39",
        property="shc",
        rock_group="carbonate",
        required_inputs=("PHIN", "DT", "VSH"),
        intercept=60.7,
        coefficients={"PHIN": 1186.1, "DT": 4.632, "VSH": -422.5},
        rms=3.1,
        reference="Fuchs et al. (2015), Table 3, C39",
    ),

    "C40": Equation(
        id="C40",
        property="shc",
        rock_group="carbonate",
        required_inputs=("U", "DT", "VSH"),
        intercept=-444.8,
        coefficients={"U": 10.4, "DT": 7.324, "VSH": -298.7},
        rms=4.5,
        reference="Fuchs et al. (2015), Table 3, C40",
    ),

    "C41": Equation(
        id="C41",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=-1345.9,
        coefficients={"RHOB": 227.0, "PHIN": -150.1, "U": 15.2, "DT": 8.194},
        rms=7.2,
        reference="Fuchs et al. (2015), Table 3, C41",
    ),

    "C42": Equation(
        id="C42",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "VSH"),
        intercept=2421.2,
        coefficients={"RHOB": -649.4, "PHIN": 2349.6, "U": 15.4, "VSH": -573.4},
        rms=4.4,
        reference="Fuchs et al. (2015), Table 3, C42",
    ),

    "C43": Equation(
        id="C43",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "DT", "VSH"),
        intercept=403.8,
        coefficients={"RHOB": -98.0, "PHIN": 1252.7, "DT": 4.154, "VSH": -439.9},
        rms=3.0,
        reference="Fuchs et al. (2015), Table 3, C43",
    ),

    "C44": Equation(
        id="C44",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "U", "DT", "VSH"),
        intercept=-363.7,
        coefficients={"RHOB": -28.0, "U": 11.3, "DT": 7.243, "VSH": -300.8},
        rms=4.5,
        reference="Fuchs et al. (2015), Table 3, C44",
    ),

    "C45": Equation(
        id="C45",
        property="shc",
        rock_group="carbonate",
        required_inputs=("PHIN", "U", "DT", "VSH"),
        intercept=-14.4,
        coefficients={"PHIN": 1153.3, "U": 5.2, "DT": 4.795, "VSH": -412.3},
        rms=3.0,
        reference="Fuchs et al. (2015), Table 3, C45",
    ),

    "C46": Equation(
        id="C46",
        property="shc",
        rock_group="carbonate",
        required_inputs=("RHOB", "PHIN", "U", "DT", "VSH"),
        intercept=584.0,
        coefficients={"RHOB": -194.4, "PHIN": 1249.6, "U": 10.9, "DT": 4.025, "VSH": -435.9},
        rms=2.8,
        reference="Fuchs et al. (2015), Table 3, C46",
    ),
# clastic 
    "C47": Equation(
        id="C47",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB",),
        intercept=4969.1,
        coefficients={"RHOB": -1558.9}, 
        rms=16.0,
        reference="Fuchs et al. (2015), Table 3, C47",
    ),

    "C48": Equation(
        id="C48",
        property="shc",
        rock_group="clastic",
        required_inputs=("PHIN",),
        intercept=579.9,
        coefficients={"PHIN": 3007.8},
        rms=9.0,
        reference="Fuchs et al. (2015), Table 3, C48",
    ),

    "C49": Equation(
        id="C49",
        property="shc",
        rock_group="clastic",
        required_inputs=("U",),
        intercept=1968.5,
        coefficients={"U": -101.8},
        rms=27.7,
        reference="Fuchs et al. (2015), Table 3, C49",
    ),

    "C50": Equation(
        id="C50",
        property="shc",
        rock_group="clastic",
        required_inputs=("DT",),
        intercept=-592.0,
        coefficients={"DT": 7.253},
        rms=5.9,
        reference="Fuchs et al. (2015), Table 3, C50",
    ),

    "C51": Equation(
        id="C51",
        property="shc",
        rock_group="clastic",
        required_inputs=("VSH",),
        intercept=1228.9,
        coefficients={"VSH": 27.2},
        rms=31.5,
        reference="Fuchs et al. (2015), Table 3, C51",
    ),

    "C52": Equation(
        id="C52",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN"),
        intercept=1815.8,
        coefficients={"RHOB": -458.5, "PHIN": 2372.0},
        rms=7.8,
        reference="Fuchs et al. (2015), Table 3, C52",
    ),

    "C53": Equation(
        id="C53",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "U"),
        intercept=5370.9,
        coefficients={"RHOB": -1893.8, "U": 56.0},
        rms=14.9,
        reference="Fuchs et al. (2015), Table 3, C53",
    ),

    "C54": Equation(
        id="C54",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "DT"),
        intercept=-617.7,
        coefficients={"RHOB": 7.8, "DT": 7.281},
        rms=5.9,
        reference="Fuchs et al. (2015), Table 3, C54",
    ),

    "C55": Equation(
        id="C55",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "VSH"),
        intercept=5176.2,
        coefficients={"RHOB": -1598.4, "VSH": -206.8},
        rms=15.5,
        reference="Fuchs et al. (2015), Table 3, C55",
    ),

    "C56": Equation(
        id="C56",
        property="shc",
        rock_group="clastic",
        required_inputs=("PHIN", "U"),
        intercept=939.5,
        coefficients={"PHIN": 2813.3, "U": -44.5},
        rms=6.6,
        reference="Fuchs et al. (2015), Table 3, C56",
    ),

    "C57": Equation(
        id="C57",
        property="shc",
        rock_group="clastic",
        required_inputs=("PHIN", "DT"),
        intercept=-411.2,
        coefficients={"PHIN": 517.1, "DT": 6.088},
        rms=5.7,
        reference="Fuchs et al. (2015), Table 3, C57",
    ),

    "C58": Equation(
        id="C58",
        property="shc",
        rock_group="clastic",
        required_inputs=("PHIN", "VSH"),
        intercept=755.3,
        coefficients={"PHIN": 3225.8, "VSH": -410.7},
        rms=4.8,
        reference="Fuchs et al. (2015), Table 3, C58",
    ),

    "C59": Equation(
        id="C59",
        property="shc",
        rock_group="clastic",
        required_inputs=("U", "DT"),
        intercept=-507.2,
        coefficients={"U": -7.7, "DT": 7.133},
        rms=5.8,   
        reference="Fuchs et al. (2015), Table 3, C59",
    ),

    "C60": Equation(
        id="C60",
        property="shc",
        rock_group="clastic",
        required_inputs=("U", "VSH"),
        intercept=1898.3,
        coefficients={"U": -109.8, "VSH": 232.6},
        rms=27.3,
        reference="Fuchs et al. (2015), Table 3, C60",
    ),

    "C61": Equation(
        id="C61",
        property="shc",
        rock_group="clastic",
        required_inputs=("DT", "VSH"),
        intercept=-517.5,
        coefficients={"DT": 7.381, "VSH": -196.3},
        rms=4.5,
        reference="Fuchs et al. (2015), Table 3, C61",
    ),

    "C62": Equation(
        id="C62",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U"),
        intercept=708.5,
        coefficients={"RHOB": 104.6, "PHIN": 2930.8, "U": -50.8},
        rms=6.6,
        reference="Fuchs et al. (2015), Table 3, C62",
    ),

    "C63": Equation(
        id="C63",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "DT"),
        intercept=-267.3,
        coefficients={"RHOB": -40.4, "PHIN": 549.3, "DT": 5.872},
        rms=5.7,
        reference="Fuchs et al. (2015), Table 3, C63",
    ),

    "C64": Equation(
        id="C64",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "VSH"),
        intercept=1820.9,
        coefficients={"RHOB": -398.1, "PHIN": 2664.2, "VSH": -392.8},
        rms=2.7,
        reference="Fuchs et al. (2015), Table 3, C64",
    ),

    "C65": Equation(
        id="C65",
        property="shc",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "DT"),
        intercept=-16.6,
        coefficients={"PHIN": 1022.3, "U": -19.7, "DT": 4.642},
        rms=5.2,
        reference="Fuchs et al. (2015), Table 3, C65",
    ),

    "C66": Equation(
        id="C66",
        property="shc",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "VSH"),
        intercept=949.1,
        coefficients={"PHIN": 3064.6, "U": -27.9, "VSH": -336.7},
        rms=3.2,
        reference="Fuchs et al. (2015), Table 3, C66",
    ),

    "C67": Equation(
        id="C67",
        property="shc",
        rock_group="clastic",
        required_inputs=("PHIN", "DT", "VSH"),
        intercept=59.3,
        coefficients={"PHIN": 1535.8, "DT": 3.989, "VSH": -302.1},
        rms=2.4,
        reference="Fuchs et al. (2015), Table 3, C67",
    ),

    "C68": Equation(
        id="C68",
        property="shc",
        rock_group="clastic",
        required_inputs=("U", "DT", "VSH"),
        intercept=-551.2,
        coefficients={"U": 3.3, "DT": 7.438, "VSH": -204.2},
        rms=4.5,
        reference="Fuchs et al. (2015), Table 3, C68",
    ),

    "C69": Equation(
        id="C69",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "DT", "VSH"),
        intercept=-403.0,
        coefficients={"RHOB": -34.7, "DT": 7.259, "VSH": -197.7},
        rms=4.5,
        reference="Fuchs et al. (2015), Table 3, C69",
    ),

    "C70": Equation(
        id="C70",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "DT"),
        intercept=-1029.5,
        coefficients={"RHOB": 188.1, "U": -16.3, "DT": 7.664},
        rms=5.7,
        reference="Fuchs et al. (2015), Table 3, C70",
    ),

    "C71": Equation(
        id="C71",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "VSH"),
        intercept=6243.8,
        coefficients={"RHOB": -2294.3, "U": 106.7, "VSH": -508.2},
        rms=12.5,
        reference="Fuchs et al. (2015), Table 3, C71",
    ),

    "C72": Equation(
        id="C72",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "DT"),
        intercept=-744.8,
        coefficients={"RHOB": 289.8, "PHIN": 1181.7, "U": -34.9, "DT": 5.072},
        rms=5.0,
        reference="Fuchs et al. (2015), Table 3, C72",
    ),

    "C73": Equation(
        id="C73",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "VSH"),
        intercept=1726.4,
        coefficients={"RHOB": -351.6, "PHIN": 2704.8, "U": -4.3, "VSH": -383.4},
        rms=2.7,
        reference="Fuchs et al. (2015), Table 3, C73",
    ),

    "C74": Equation(
        id="C74",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "DT", "VSH"),
        intercept=891.3,
        coefficients={"RHOB": -221.4, "PHIN": 1804.4, "DT": 2.618, "VSH": -329.5},
        rms=1.7,
        reference="Fuchs et al. (2015), Table 3, C74",
    ),

    "C75": Equation(
        id="C75",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "U", "DT", "VSH"),
        intercept=14.3,
        coefficients={"RHOB": -206.4, "U": 14.7, "DT": 6.908, "VSH": -239.8},
        rms=4.4,
        reference="Fuchs et al. (2015), Table 3, C75",
    ),

    "C76": Equation(
        id="C76",
        property="shc",
        rock_group="clastic",
        required_inputs=("PHIN", "U", "DT", "VSH"),
        intercept=319.3,
        coefficients={"PHIN": 1853.0, "U": -13.9, "DT": 3.052, "VSH": -290.9},
        rms=1.9,
        reference="Fuchs et al. (2015), Table 3, C76",
    ),

    "C77": Equation(
        id="C77",
        property="shc",
        rock_group="clastic",
        required_inputs=("RHOB", "PHIN", "U", "DT", "VSH"),
        intercept=814.6,
        coefficients={"RHOB": -182.9, "PHIN": 1840.7, "U": -3.6, "DT": 2.611, "VSH": -321.8},
        rms=1.7,
        reference="Fuchs et al. (2015), Table 3, C77",
    ),
}


def get_equation(equation_id: str) -> Equation:
    """
    Return the equation with the given ID.

    Raises
    ------
    KeyError
        If *equation_id* is not found in :data:`EQUATIONS`.
    """
    try:
        return EQUATIONS[equation_id]
    except KeyError:
        raise KeyError(
            f"Unknown equation: {equation_id!r}. "
            f"Valid IDs are A1-A77, B1-B77, C1-C77."
        )


def list_equations() -> List[Equation]:
    """Return all equations as a list."""
    return list(EQUATIONS.values())


def list_by_property(prop: str) -> List[Equation]:
    """
    Return all equations for one thermal property.

    Parameters
    ----------
    prop : str
        One of "tc", "td", or "shc".
    """
    return [eq for eq in EQUATIONS.values() if eq.property == prop]


def list_by_rock_group(rock_group: str) -> List[Equation]:
    """
    Return all equations for one rock group.

    Parameters
    ----------
    rock_group : str
        One of "clastic", "carbonate", or "evaporite".
    """
    return [eq for eq in EQUATIONS.values() if eq.rock_group == rock_group]