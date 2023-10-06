"""
Author: Project Somedays
"""
import PySimpleGUI as sg
#TODO: Implement searching for position within a string

def main():
    # invite the user to enter the string
    text = sg.PopupGetText("What string do I need to count?")
    sg.Popup(f"Length of text {text} = {len(text)}")


if __name__ == "__main__":
    main()
