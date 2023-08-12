from enum import Enum
from math import pi
from decimal import Decimal
from typing import Callable, Protocol

# TODO: optional Decimal place setting


class Units(Enum):
    PI_RAD = "pi_radians"
    RAD = "radians"
    DEG = "deg"


class Categories(Enum):
    ANGLES = "angles"


CONVERSIONS = {
    Categories.ANGLES: {
        Units.PI_RAD: 1 / Decimal("180"),
        Units.RAD: Decimal(str(pi)) / Decimal("180"),
        Units.DEG: Decimal(str(pi)) / Decimal("180"),
    }
}


class Input_Getter(Protocol):
    def get_user_input(self):
        ...

    def validate_user_input(self):
        ...


class Input_Getter_CMD_Line:
    def get_user_input(self):
        user_input_list: list[str] = input(
            "Enter your request in the following format: source_amount source_unit to target_unit"
        ).split(" ")

        if self.validate_input(user_input_list):
            return {
                "amt": Decimal(user_input_list[0]),
                "from": user_input_list[1],
                "to": user_input_list[3],
            }

    def validate_input(self, user_input_list: list[str]) -> bool:
        if user_input_list[1] not in [x.value for x in Units]:
            raise ValueError(f"UnKnown unit: {user_input_list[1]}")
        if user_input_list[2] != "to":
            raise ValueError("Please follow the strict format amt unit_from to unit_to")
        if user_input_list[3] not in [x.value for x in Units]:
            raise ValueError(f"UnKnown unit: {user_input_list[3]}")
        return True


def convert(amt: Decimal, from: Units, to: Units) -> Decimal:
    raise NotImplementedError("Uh Oh! You haven't got this far yet!")


def main():
    # get user input
    input_getter = Input_Getter_CMD_Line()
    user_input = input_getter.get_user_input()
    print(user_input)
    # result = convert(user_input["amt"], user_input["from"], user_input["to"])


if __name__ == "__main__":
    main()
