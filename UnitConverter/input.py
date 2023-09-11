from typing import Protocol
from decimal import Decimal
from consts import Units
from dataclasses import dataclass


@dataclass
class UserInput:
    amt: Decimal
    unit_from: str
    unit_to: str
    dp: int

    @property
    def conversion_string(self) -> str:
        return f"{self.unit_from} to {self.unit_to}"


class Input_Getter(Protocol):
    def get_user_input(self) -> UserInput:
        ...


class Input_Getter_CMD_Line:
    def get_user_input(self) -> UserInput | None:
        user_input_list: list[str] = input(
            "Enter your request in the following format: source_amount source_unit to target_unit: "
        ).split(" ")
        dp = None

        if self.validate_input(user_input_list):
            if len(user_input_list) > 4:
                dp = int(user_input_list[4][: user_input_list[4].find("dp")])
            else:
                dp = 2
            return UserInput(
                amt=Decimal(user_input_list[0]),
                unit_from=user_input_list[1],
                unit_to=user_input_list[3],
                dp=dp,
            )
        else:
            return None

    def validate_input(self, user_input_list: list[str]) -> bool:
        if user_input_list[1] not in [x.value for x in Units]:
            raise ValueError(f"UnKnown unit: {user_input_list[1]}")
        if user_input_list[2] != "to":
            raise ValueError("Please follow the strict format amt unit_from to unit_to")
        if user_input_list[3] not in [x.value for x in Units]:
            raise ValueError(f"UnKnown unit: {user_input_list[3]}")
        return True
