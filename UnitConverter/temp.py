from decimal import Decimal


def deg_F_to_C(amt: Decimal) -> Decimal:
    return Decimal("5") / Decimal("9") * (amt - 32)


def deg_C_to_F(amt: Decimal) -> Decimal:
    return Decimal("9") / Decimal("5") * amt + 32


def deg_K_to_C(amt: Decimal) -> Decimal:
    return amt - Decimal("273.15")


def deg_C_to_K(amt: Decimal) -> Decimal:
    return amt + Decimal("273.15")


def deg_K_to_F(amt: Decimal) -> Decimal:
    return deg_C_to_F(deg_K_to_C(amt))


def deg_F_to_K(amt: Decimal) -> Decimal:
    return deg_C_to_K(deg_F_to_C(amt))
