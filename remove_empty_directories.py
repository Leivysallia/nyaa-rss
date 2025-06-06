import os


# test_path = "S:/py_test_path"
fin_asw = "S:/crimson/fin/ASW"
fin = "S:/crimson/fin"
_path = fin_asw


def check_for_empty(root):
    for dirpath, dir_names, filenames in os.walk(root):
        if not filenames and not dir_names and dirpath != root:
            return True
    return False


def remove_empty_directories(root):
    for dirpath, dir_names, filenames in os.walk(root):
        if not filenames and not dir_names and dirpath != root:
            try:
                os.rmdir(dirpath)
                print(f"{dirpath} empty; removing.")
            except PermissionError:
                print(f"PermissionError; {dirpath} not removed!")


def remove_empties(run_path):
    while check_for_empty(run_path):
        remove_empty_directories(run_path)


if check_for_empty(_path):
    remove_empties(_path)
else:
    print(f"There are no empty directories in {_path}...")
