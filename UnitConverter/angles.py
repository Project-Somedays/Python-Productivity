from decimal import Decimal
from math import pi


def deg_to_pi_rad(amt: Decimal) -> Decimal:
    return amt / Decimal("180")


def pi_rad_to_deg(amt: Decimal) -> Decimal:
    return amt * Decimal("180")


def deg_to_rad(amt: Decimal) -> Decimal:
    return deg_to_pi_rad(amt) * Decimal(str(pi))


def rad_to_deg(amt: Decimal) -> Decimal:
    return pi_rad_to_deg(amt) / Decimal(str(pi))


def rad_to_pi_rad(amt: Decimal) -> Decimal:
    return amt / Decimal(str(pi))


def pi_rad_to_rad(amt: Decimal) -> Decimal:
    return amt * Decimal(str(pi))
