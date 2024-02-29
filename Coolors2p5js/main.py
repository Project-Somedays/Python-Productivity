import PySimpleGUI as sg
import pyperclip

def main():
    hex_strings = sg.PopupGetText("Please enter the string of hexes")
    hex_string_list = hex_strings.split(", ")
    for_copy_pasting = ", ".join([f"'{x}'" for x in hex_string_list])
    pyperclip.copy(for_copy_pasting)
    sg.popup_auto_close("Hex values copied to clipboard", auto_close_duration=2)

if __name__ == '__main__':
    main()