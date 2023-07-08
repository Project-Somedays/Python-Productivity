"""
Author: Project Somedays
"""
import PySimpleGUI as sg
from enum import Enum
from decimal import Decimal
from typing import Any

# FIXME: Not recognising when units are changed


class U(Enum):
    KM = "km"
    M = "m"
    CM = "cm"
    MM = "mm"
    UM = "μm"
    NM = "nm"
    YD = "yd"
    FT = "ft"
    IN = "in"
    HH = "hh"
    BARLEYCORN = "barleycorn"
    CH = "ch"
    FUR = "fur"
    MI = "mi"


L_CONV = {
    U.KM.value: Decimal("1000"),
    U.M.value: Decimal("1"),
    U.CM.value: Decimal("0.01"),
    U.MM.value: Decimal("0.001"),
    U.UM.value: Decimal("0.000001"),
    U.NM.value: Decimal("0.000000001"),
    U.YD.value: Decimal("1"),
    U.FT.value: Decimal("3"),
    U.HH.value: Decimal(1) / Decimal(9),
    U.IN.value: Decimal(1) / Decimal(36),
    U.BARLEYCORN.value: Decimal(1) / Decimal(108),
    U.CH.value: Decimal("22"),
    U.FUR.value: Decimal("220"),
    U.MI.value: Decimal("1760"),
}

L_CONV_RATE = {U.M.value: Decimal(1) / Decimal("0.9144"), U.YD.value: Decimal("0.9144")}

METRIC_UNITS = [U.KM.value, U.M.value, U.CM.value, U.MM.value, U.UM.value, U.NM.value]

IMPERIAL_UNITS = [
    U.MI.value,
    U.FUR.value,
    U.CH.value,
    U.YD.value,
    U.FT.value,
    U.HH.value,
    U.IN.value,
    U.BARLEYCORN.value,
]


class K(Enum):
    TO_CONVERT = "to_convert"
    CONVERTED = "converted"
    SRC_UNIT = "src_unit"
    TRGT_UNIT = "dst_unit"
    CONVERT = "convert"
    CANCEL = "Cancel"


def convert(src_val: Decimal, src_unit: str, target_unit: str) -> str:
    src_si = src_val / L_CONV[src_unit]
    src_is_metric = src_unit in METRIC_UNITS
    trgt_is_metric = target_unit in METRIC_UNITS
    # if the same unit, then just divide by the conversion rate back to SI
    if (src_is_metric and trgt_is_metric) or (not src_is_metric and not trgt_is_metric):
        trgt_val = src_val / L_CONV[target_unit]
    # if different, convert to SI and then
    else:
        trgt_val = src_si / L_CONV_RATE[src_unit] / L_CONV[target_unit]

    return f"{trgt_val:.3f}"


def get_layout() -> list[Any]:
    return [
        [
            sg.In(key=K.TO_CONVERT.value, size=(8, 1)),
            sg.InputCombo(
                values=[l.value for l in U], size=(4, 1), key=K.SRC_UNIT.value
            ),
            sg.T("-->"),
            sg.T(key=K.CONVERTED.value),
            sg.InputCombo(
                values=[l.value for l in U], size=(4, 1), key=K.TRGT_UNIT.value
            ),
        ],
        [sg.B("Convert", key=K.CONVERT.value), sg.Cancel()],
    ]


def main():
    """Do the needful"""
    window = sg.Window(title="Unit Converter", layout=get_layout())
    while True:
        event, values = window.read()
        if event in [K.CANCEL.value, sg.WIN_CLOSED]:
            break
        elif event == K.CONVERT.value:
            src_unit = values[K.SRC_UNIT.value]
            src_val = Decimal(values[K.TO_CONVERT.value])
            target_unit = values[K.TRGT_UNIT.value]
            target_val = convert(src_val, src_unit, target_unit)
            window[K.CONVERTED.value].update(target_val)
        else:
            pass


if __name__ == "__main__":
    main()
