"""
Creates a copy of the template in a target folder
"""

import os
import shutil
import PySimpleGUI as sg

TEMPLATE_PATH = r"C:\Users\proje\OneDrive\Documents\Python-Productivity\ProcessingProjectGenerator\template.pde"


def get_folder_and_filename() -> dict[str, str]:
    layout = [
        [sg.T("Project Name: "), sg.In(key="PROJ")],
        [
            sg.T("Choose project root folder"),
            sg.FolderBrowse(key="FOLDER"),
            sg.T(key="PATH"),
        ],
        [sg.Submit(), sg.Cancel()],
    ]
    window = sg.Window(title="Set Project name and Folder", layout=layout)
    while True:
        event, values = window.read()
        if event in ["Cancel", sg.WIN_CLOSED]:
            break
        elif event == "FOLDER":
            window["PATH"].update(values["FOLDER"])
        elif event == "Submit":
            break
        else:
            pass
    window.close()
    return values


def main():
    print("Getting the project name and target")
    user_input: dict[str, str] = get_folder_and_filename()
    project_name = user_input["PROJ"].replace(" ", "_")
    target = user_input["FOLDER"]
    print("Making folder")
    new_path = os.path.join(target, project_name)
    print(f"Proposed folder path: {new_path}")
    if os.path.exists(new_path):
        print("That already exists! Belay that override!")
        return
    os.mkdir(new_path)
    first_iteration_path = os.path.join(new_path, project_name + "_01")
    os.mkdir(first_iteration_path)
    new_file_path = os.path.join(first_iteration_path, project_name + "_01.pde")
    print(f"Copying the template file into new directory: {new_file_path}")
    shutil.copy(TEMPLATE_PATH, new_file_path)
    print("Opening the file")
    os.startfile(new_file_path)


if __name__ == "__main__":
    main()
