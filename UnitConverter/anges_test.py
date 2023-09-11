from angles import (
    deg_to_rad,
    deg_to_pi_rad,
    rad_to_deg,
    rad_to_pi_rad,
    pi_rad_to_deg,
    pi_rad_to_rad,
)
from math import pi
from decimal import Decimal


def test_deg_to_rad():
    assert deg_to_rad(Decimal("180")) == Decimal(str(pi))


def test_deg_to_pi_rad():
    assert deg_to_pi_rad(Decimal("180")) == 1


def test_rad_to_deg():
    assert rad_to_deg(Decimal(str(pi))) == 180


def test_pi_rad_to_deg():
    assert pi_rad_to_deg(Decimal("1")) == Decimal("180")


def test_rad_to_pi_rad():
    assert rad_to_pi_rad(Decimal(str(pi))) == 1


def test_pi_rad_to_rad():
    assert pi_rad_to_rad(Decimal("1")) == Decimal(str(pi))
