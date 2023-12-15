"""
Creates a copy of the template in a target folder
"""
from enum import StrEnum, auto
from icecream import ic
import os
import shutil
import PySimpleGUI as sg

TEMPLATE_PATH = r"C:\Users\proje\OneDrive\Documents\Python-Productivity\ProcessingProjectGenerator\template.pde"


class K(StrEnum):
    PROJECTNAME = auto()
    FOLDER = auto()
    PATHVIEW = auto()
    ISBASEPROJECT = auto()
    SUBMIT = "Submit"
    CANCEL = "Cancel"


def get_folder_and_filename() -> dict[str, str]:
    layout = [
        [sg.T("Project Name: "), sg.In(key=K.PROJECTNAME.value)],
        [
            sg.T("Choose project root folder"),
            sg.FolderBrowse(key=K.FOLDER.value),
        ],
        [
            sg.T(key=K.PATHVIEW.value),
            sg.Checkbox("New Base Project?", key=K.ISBASEPROJECT.value, default=True),
        ],
        [sg.Submit(), sg.Cancel()],
    ]
    window = sg.Window(title="Set Project name and Folder", layout=layout)
    while True:
        event, values = window.read()
        if event in ["Cancel", sg.WIN_CLOSED]:
            break
        elif event == "FOLDER":
            window["PATH"].update(values[K.FOLDER.value])
        elif event == "Submit":
            break
        else:
            pass
    window.close()
    return values


def main():
    print("Getting the project name and target")
    user_input: dict[str, str] = get_folder_and_filename()
    project_name = user_input[K.PROJECTNAME.value].replace(" ", "_")
    target = user_input[K.FOLDER.value]

    print("Making folder")
    if user_input[K.ISBASEPROJECT.value]:
        new_path = os.path.join(target, project_name)
    else:
        new_path = os.path.join(target, project_name + "_1")
    ic(new_path)
    if os.path.exists(new_path):
        print("That already exists! Belay that override!")
        return

    os.mkdir(new_path)
    print("Copying file")
    if user_input[K.ISBASEPROJECT.value]:
        print("Making subfolder")
        first_iteration_path = os.path.join(new_path, project_name + "_01")
        os.mkdir(first_iteration_path)
        new_file_path = os.path.join(first_iteration_path, project_name + "_01.pde")
    else:
        new_file_path = os.path.join(new_path, project_name + "_01.pde")
    print("Copying the template file into new directory")
    ic(new_file_path)
    shutil.copy(TEMPLATE_PATH, new_file_path)
    print("Opening the file")
    os.startfile(new_file_path)


if __name__ == "__main__":
    main()
