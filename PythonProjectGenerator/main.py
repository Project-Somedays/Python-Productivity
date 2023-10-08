"""
Creates a copy of the template in a target folder
"""

import PySimpleGUI as sg
import os
import shutil
import subprocess

TEMPLATE_PATH = r"C:\Users\proje\OneDrive\Documents\Python-Productivity\PythonProjectGenerator\template.py"


def get_folder_and_filename() -> dict[str, str]:
    layout = [
        [sg.T("Project Name: "), sg.In(key="PROJ")],
        [sg.FolderBrowse(key="FOLDER")],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window(title="Set Project name and Folder", layout=layout)
    event, value = window.read()
    window.close()
    return value


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
    new_file_path = os.path.join(new_path, "main.py")
    print(f"Copying the template file into new directory: {new_file_path}")
    shutil.copy(TEMPLATE_PATH, new_file_path)
    
    try:
    # Use the 'code' command to open the specified directory in VS Code
        subprocess.Popen([r"C:\Users\proje\AppData\Local\Programs\Microsoft VS Code\Code.exe", new_path])
    except FileNotFoundError:
        print("Visual Studio Code (code command) not found. Make sure it's in your system's PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
