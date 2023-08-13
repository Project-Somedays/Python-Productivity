from temp import deg_F_to_C, deg_C_to_F, deg_K_to_C, deg_K_to_F, deg_C_to_K, deg_F_to_K
from decimal import Decimal


def test_deg_F_to_C():
    assert deg_F_to_C(Decimal("32")) == 0
    assert deg_F_to_C(Decimal("77")) == 25
    assert deg_F_to_C(Decimal("356")) == 180


def test_deg_C_to_F():
    assert deg_C_to_F(Decimal("0")) == 32
    assert deg_C_to_F(Decimal("25")) == 77
    assert deg_C_to_F(Decimal("40")) == 104


def test_deg_C_to_K():
    assert deg_C_to_K(Decimal("0")) == Decimal("273.15")
    assert deg_C_to_K(Decimal("-273.15")) == 0


def test_deg_K_to_C():
    assert deg_K_to_C(Decimal("273.15")) == 0
    assert deg_K_to_C(Decimal("0")) == Decimal("-273.15")


def test_deg_K_to_F():
    assert deg_K_to_F(Decimal("273.15")) == 32


def test_deg_F_to_K():
    assert deg_F_to_K(Decimal("32")) == Decimal("273.15")
