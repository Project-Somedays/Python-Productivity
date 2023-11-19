import PySimpleGUI as sg
import os
from icecream import ic
import shutil

def main():
    new_dir_path = ""
    to_iterate_fp = sg.PopupGetFolder("Choose a project folder to iterate on")
    ic(to_iterate_fp)
    
    while True:
        to_iterate_dirname = os.path.basename(to_iterate_fp)
        ic(to_iterate_dirname)
        
        # get the folder name and replace all the spaces with _
        new_folder_name = sg.PopupGetText("Choose your new folder name: ", default_text=os.path.basename(to_iterate_fp)).replace(" ", "_")
        ic(new_folder_name)
        
        parent_folder = os.path.dirname(to_iterate_fp)
        ic(parent_folder)
        
        new_dir_path = os.path.join(parent_folder, new_folder_name)
        ic(new_dir_path)

        if not os.path.exists(new_dir_path):
            shutil.copytree(to_iterate_fp,new_dir_path)
            break

    print("Renaming the project file to match the destination folder")
    # rename the file inside that has the old folder name
    to_rename = os.path.join(new_dir_path, to_iterate_dirname + ".pde")
    to_rename_to = os.path.join(new_dir_path, new_folder_name + ".pde")
    os.rename(to_rename, to_rename_to)

    # delete everything without a .pde extension
    print("Removing everything that isn't a .pde file")
    for each in os.listdir(new_dir_path):
        each_fn, each_ext = os.path.splitext(each)
        if each_ext == ".pde":
            continue
        print(f"Removing {each}")
        os.remove(os.path.join(new_dir_path,each))

    print("Opening the file")
    os.startfile(to_rename_to)


            




    



if __name__ == '__main__':
    main()