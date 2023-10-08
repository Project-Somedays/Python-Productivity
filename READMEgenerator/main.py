"""
Author: Project Somedays

Effectively walks through creative coding repositories and makes links to files using their preview.
Because I'm only travelling one step into each directory, I've don't need a walk.
Plus, they were doing my head in.
"""
import os
import PySimpleGUI as sg
from icecream import ic

def convert_subdirectory_to_link(base_dir: str, dir: str) -> str:
    """Returns link image"""
    image_name = f"{base_dir}/{dir}.png"
    return f'<a href = "{base_dir}/{dir}"><img src="{image_name}" width="100" alt="{image_name}"></a>'

def convert_directory_to_link(dir: str) -> str:
    return f'## [{dir}]({dir.replace(" ","%20")})'

def overwrite_filecontents(readme_file_path: str, lines: str) -> None:
    with open(readme_file_path, "w") as fh:
        fh.writelines("\n".join(lines))


base_exclude = [".git"]

def main():
    """Do the needful"""
    base = sg.PopupGetFolder("Choose the base root of the walk")
    target_readme_file = sg.PopupGetFile("Please choose the target README.md file to overwrite")
    if os.path.splitext(target_readme_file)[1] != ".md":
        raise ValueError("Not a .md file!")
    ic(base)
    project_folders = [dir for dir in os.listdir(base) if os.path.isdir(os.path.join(base,dir)) and dir not in base_exclude] #if os.path.isdir(dir)]
    ic(project_folders)

    lines = ["# Creative-Coding-Processing", "Creative Coding Projects written in Processing. Mostly in progress."]

    for project_folder in project_folders:
        lines.append(convert_directory_to_link(project_folder))
        project_subfolder_path = os.path.join(base, project_folder)
        ic(project_subfolder_path)
        project_subfolders = [dir for dir in os.listdir(project_subfolder_path) if os.path.isdir(os.path.join(project_subfolder_path,dir))]
        ic(project_subfolders)
        for project_subfolder in project_subfolders:
            lines.append(convert_subdirectory_to_link(base_dir = project_folder, dir = project_subfolder))

    ic(lines)
    print("Constructing README file")
    overwrite_filecontents(readme_file_path=target_readme_file, lines = lines)
    
    

    


if __name__ == "__main__":
    main()
