from math import pi
from decimal import Decimal
from typing import Callable
from dataclasses import dataclass
from temp import deg_C_to_F, deg_F_to_C, deg_C_to_K, deg_F_to_K, deg_K_to_C, deg_K_to_F
from input import Input_Getter_CMD_Line, UserInput
from consts import Units

# TODO: optional Decimal place setting
# TODO: work out degrees


@dataclass
class Result:
    from_amt: Decimal
    to_amt: Decimal
    from_unit: str
    to_unit: str
    dp: int

    def __repr__(self):
        # amt = f"{self.to_amt:.self.dpf}"
        return f"{self.from_amt} {self.from_unit} = {self.to_amt:.{self.dp}f} {self.to_unit}"


CONVERSIONS: dict[str, Callable[[Decimal], Decimal]] = {
    Units.PI_RAD.value: lambda x: x * Decimal("180"),  # type: ignore
    Units.RAD.value: lambda x: x * Decimal("180") / Decimal(str(pi)),  # type: ignore
    Units.DEG.value: lambda x: x * Decimal(str(pi)) / Decimal("180"),  # type: ignore
    Units.DEG_C.value: deg_C_to_F,  # type: ignore
    Units.DEG_F.value: deg_F_to_C,  # type: ignore
}

CONVERSION_STRINGS_TO_FNS: dict[str, Callable[[Decimal], Decimal]] = {
    f"{Units.DEG_C.value} to {Units.DEG_F.value}": deg_C_to_F,
    f"{Units.DEG_F.value} to {Units.DEG_C.value}": deg_F_to_C,
    f"{Units.DEG_C.value} to {Units.DEG_K.value}": deg_C_to_K,
    f"{Units.DEG_K.value} to {Units.DEG_C.value}": deg_K_to_C,
    f"{Units.DEG_F.value} to {Units.DEG_K.value}": deg_F_to_K,
    f"{Units.DEG_K.value} to {Units.DEG_F.value}": deg_K_to_F,
}


def convert2(
    amt_to_convert: Decimal, unit_from: str, unit_to: str, dp: int = 2
) -> Result:
    return Result(
        from_amt=amt_to_convert,
        from_unit=unit_from,
        to_unit=unit_to,
        dp=dp,
        to_amt=CONVERSION_STRINGS_TO_FNS[f"{unit_from} to {unit_to}"](
            amt_to_convert
        ),
    )


def convert(
    amt_to_convert: Decimal, unit_from: str, unit_to: str, dp: int = 2
) -> Result:
    return Result(
        from_amt=amt_to_convert,
        from_unit=unit_from,
        to_amt=CONVERSIONS[unit_from](amt_to_convert),
        to_unit=unit_to,
        dp=dp,
    )


def main():
    # get user input
    input_getter = Input_Getter_CMD_Line()
    user_input: UserInput = input_getter.get_user_input()
    # print(user_input)
    result = convert2(
        amt_to_convert=user_input.amt,
        unit_from=user_input.unit_from,
        unit_to=user_input.unit_to,
        dp=user_input.dp,
    )
    print(result)


if __name__ == "__main__":
    main()
