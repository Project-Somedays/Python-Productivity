from typing import Protocol, Callable
from decimal import Decimal
from enum import Enum


class Input_Getter(Protocol):
    def get_user_input(self):
        ...


class Units(Enum):
    PI_RAD = "pi_rad"
    RAD = "rad"
    DEG = "deg"
    DEG_C = "degC"
    DEG_F = "degF"
    DEG_K = "degK"


CONVERSIONS: dict[str, Callable[[Decimal], Decimal]] = {
    Units.PI_RAD.value: lambda x: x * Decimal("180"),  # type: ignore
    Units.RAD.value: lambda x: x * Decimal("180") / Decimal(str(pi)),  # type: ignore
    Units.DEG.value: lambda x: x * Decimal(str(pi)) / Decimal("180"),  # type: ignore
    Units.DEG_C.value: deg_C_to_F,  # type: ignore
    Units.DEG_F.value: deg_F_to_C,  # type: ignore
}


class Input_Getter_CMD_Line:
    def get_user_input(self):
        user_input_list: list[str] = input(
            "Enter your request in the following format: source_amount source_unit to target_unit: "
        ).split(" ")

        if self.validate_input(user_input_list):
            return {
                "amt": Decimal(user_input_list[0]),
                "from": user_input_list[1],
                "to": user_input_list[3],
                "dp": 2
                if not user_input_list[4]
                else int(user_input_list[4][: user_input_list[4].find("dp")]),
            }

    def validate_input(self, user_input_list: list[str]) -> bool:
        if user_input_list[1] not in [x.value for x in Units]:
            raise ValueError(f"UnKnown unit: {user_input_list[1]}")
        if user_input_list[2] != "to":
            raise ValueError("Please follow the strict format amt unit_from to unit_to")
        if user_input_list[3] not in [x.value for x in Units]:
            raise ValueError(f"UnKnown unit: {user_input_list[3]}")
        return True
