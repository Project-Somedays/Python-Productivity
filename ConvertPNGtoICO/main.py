from PIL import Image
import PySimpleGUI as sg
import os


def main():
    logo_filename = sg.popup_get_file("What image would you like converted?")
    desired_filename = sg.popup_get_text("What would you like to call the icon?")
    target_folder = sg.popup_get_folder("Where would you like it saved?")
    target_filepath = os.path.join(target_folder, desired_filename + ".ico")
    logo = Image.open(logo_filename)

    logo.save(target_filepath, format="ICO", sizes=[(256, 256)])


if __name__ == "__main__":
    main()
