# from main import increment_name, rename_to_match_root
from main import get_new_project_filename

# def test_increment_name():
#     assert increment_name("Packing_Algorithm_Study_02") == "Packing_Algorithm_Study_03"
#     assert increment_name("Packing_Algorithm_Study_01_01") == "Packing_Algorithm_Study_01_02"
#     assert increment_name("Packing_Algorithm_Study") == "Packing_Algorithm_Study_01"
#     # assert increment_name("Packing_Algorithm_Study"))

def test_get_new_project_filename():
    file_names = ["Packing_Algorithm_Study_02.pde","Arrow.pde"]
    match_name = "Packing_Algorithm_Study_02"
    new_path = "Packing_Algorithm_Study_03"
    assert get_new_project_filename(match_name = match_name, files = file_names , new_dirpath= new_path) == r"C:\Users\proje\OneDrive\Documents\Creative-Coding-Processing\Packing_Algorithm_Study\Packing_Algorithm_Study_03\Packing_Algorithm_Study_03.pde"