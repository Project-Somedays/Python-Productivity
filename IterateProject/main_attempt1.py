import PySimpleGUI as sg
import os
from icecream import ic
import shutil

def main():
#     # choose project folder to iterate on
#     folder_path = sg.PopupGetFolder("Choose Project Folder")
#     os.chdir(folder_path)
#     os.chdir("../")
#     ic(os.getcwd())
#     # extract folder name
#     ic(folder_path)
#     folder_root_name = os.path.basename(folder_path)
#     ic(folder_root_name)
#     new_folder_root_name = increment_name(folder_root_name)
#     ic(new_folder_root_name)
#     target_path = os.path.join(os.getcwd(),new_folder_root_name)
#     ic(target_path)
#     if os.path.exists(target_path):
#         target_path = target_path + "_01"
#     shutil.copy(folder_path, target_path)
    
#     # rename the main file
#     os.chdir(target_path)
#     for each in os.listdir():
#         if os.path.splitext(each)[0] == folder_root_name:
#             os.rename(each, target_path)

# def rename_to_match_root(match_path: str, new_path: str, filenames: list[str]) -> str:
#     file_paths = [os.path.join(match_path(filename)) for filename in filenames]
#     end_of_branch = os.path.basename(match_path)
    

# def is_integer(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False


# def increment_name(name: str) -> str:
#     # find the position of 
#     ix = name.rfind("_")
#     end_substring = name[ix+1:]
#     if not is_integer(end_substring):
#         return f"{name}_01"
#     return f"{name[:ix+1]}{str(int(end_substring)+1).zfill(2)}"




if __name__ == '__main__':
    main()