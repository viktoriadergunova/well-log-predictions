# TODO ADD COMMENT

import math
import pytest
from src.equation_data import EQUATIONS, get_equation, list_equations, list_by_property, list_by_rock_group

VALID_PROPERTIES  = {"tc", "td", "shc"}
VALID_ROCK_GROUPS = {"clastic", "carbonate", "evaporite"}
VALID_LOG_COLUMNS = {"RHOB", "PHIN", "VSH", "DT","U"  }


class TestEquationStructure:

    @pytest.mark.parametrize("eq_id,eq", EQUATIONS.items())
    def test_required_inputs_is_tuple(self, eq_id, eq):
        assert isinstance(eq.required_inputs, tuple), (
            f"{eq_id}: required_inputs is {type(eq.required_inputs).__name__!r}, expected tuple"
        )

    @pytest.mark.parametrize("eq_id,eq", EQUATIONS.items())
    def test_required_inputs_are_known_columns(self, eq_id, eq):
        for col in eq.required_inputs:
            assert col in VALID_LOG_COLUMNS, (
                f"{eq_id}: unknown input {col!r} — valid columns are {VALID_LOG_COLUMNS}"
            )

    @pytest.mark.parametrize("eq_id,eq", EQUATIONS.items())
    def test_coefficients_match_required_inputs(self, eq_id, eq):
        assert set(eq.coefficients.keys()) == set(eq.required_inputs), (
            f"{eq_id}: coefficients keys {set(eq.coefficients)} "
            f"do not match required_inputs {set(eq.required_inputs)}"
        )

    @pytest.mark.parametrize("eq_id,eq", EQUATIONS.items())
    def test_intercept_is_finite(self, eq_id, eq):
        assert math.isfinite(eq.intercept), (
            f"{eq_id}: intercept is not finite: {eq.intercept}"
        )

    @pytest.mark.parametrize("eq_id,eq", EQUATIONS.items())
    def test_rms_is_non_negative(self, eq_id, eq):
        assert eq.rms >= 0, f"{eq_id}: rms is negative: {eq.rms}"

    @pytest.mark.parametrize("eq_id,eq", EQUATIONS.items())
    def test_property_is_valid(self, eq_id, eq):
        assert eq.property in VALID_PROPERTIES, (
            f"{eq_id}: property {eq.property!r} not in {VALID_PROPERTIES}"
        )

    @pytest.mark.parametrize("eq_id,eq", EQUATIONS.items())
    def test_rock_group_is_valid(self, eq_id, eq):
        assert eq.rock_group in VALID_ROCK_GROUPS, (
            f"{eq_id}: rock_group {eq.rock_group!r} not in {VALID_ROCK_GROUPS}"
        )

    @pytest.mark.parametrize("eq_id,eq", EQUATIONS.items())
    def test_id_matches_dict_key(self, eq_id, eq):
        assert eq.id == eq_id, (
            f"Equation id field {eq.id!r} does not match dict key {eq_id!r}"
        )

    def test_all_ids_are_unique(self):
        ids = [eq.id for eq in EQUATIONS.values()]
        assert len(ids) == len(set(ids)), "Duplicate equation IDs found"


class TestHelperFunctions:
    """
    Tests for get_equation(), list_equations(), list_by_property(),
    and list_by_rock_group() in equation_data.py.
    
    """

    def test_get_equation_returns_correct(self):
        eq = get_equation("A1")
        assert eq.id == "A1"
        assert eq.property == "tc"
        assert eq.rock_group == "evaporite"

    def test_get_equation_raises_on_unknown(self):
        with pytest.raises(KeyError):
            get_equation("Z99")

    def test_list_equations_returns_all(self):
        assert len(list_equations()) == len(EQUATIONS)

    def test_list_by_property_tc(self):
        eqs = list_by_property("tc")
        assert all(eq.property == "tc" for eq in eqs)
        assert len(eqs) > 0

    def test_list_by_property_unknown(self):
        assert list_by_property("xyz") == []

    def test_list_by_rock_group_clastic(self):
        eqs = list_by_rock_group("clastic")
        assert all(eq.rock_group == "clastic" for eq in eqs)
        assert len(eqs) > 0

    def test_list_by_rock_group_unknown(self):
        assert list_by_rock_group("xyz") == []