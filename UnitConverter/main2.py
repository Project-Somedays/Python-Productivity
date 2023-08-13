from math import pi
from decimal import Decimal
from typing import Callable
from dataclasses import dataclass
from temp import deg_C_to_F, deg_F_to_C, deg_C_to_K, deg_F_to_K, deg_K_to_C
from input import Input_Getter, Input_Getter_CMD_Line, CONVERSIONS

# TODO: optional Decimal place setting
# TODO: work out degrees


@dataclass
class Result:
    amt: Decimal
    unit: str
    dp: int

    def __repr__(self):
        return f"{self.amt:.{self.dp}f} {self.unit}"


def convert(amt_to_convert: Decimal, unit_from: str, unit_to: str) -> Result:
    return Result(amt=CONVERSIONS[unit_from](amt_to_convert), unit=unit_to)


def main():
    # get user input
    input_getter = Input_Getter_CMD_Line()
    user_input: dict[str, str | Decimal] = input_getter.get_user_input()
    print(user_input)
    result = convert(user_input["amt"], user_input["from"], user_input["to"])
    print(result)


if __name__ == "__main__":
    main()
