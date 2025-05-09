import os
import re


asw = r"^\[ASW\].*$"
error_set = set([])
full_set = set([])
videos = "S:/Dropbox/Videos"
basedir = "S:/crimson/fin/ASW"
nyaa = "S:/crimson/fin/ASW/nyaa/ASW"


def check_file():
    for fn in os.listdir(basedir):
        if os.path.isfile(os.path.join(basedir, fn)) and re.match(asw, fn, flags=re.I):
            return True
    return False


def clear_console():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def create_nyaa():
    try:
        os.makedirs(nyaa)
        print(f"Created folder {nyaa}")
    except FileExistsError:
        pass


def sort_nyaa():
    for fn in os.listdir(basedir):
        if os.path.isfile(os.path.join(basedir, fn)):
            if re.match(asw, fn, flags=re.I):
                new_name = re.sub(r"\[[a-z0-9]+\]", "", fn, flags=re.I)
                new_name = re.sub(r"^", "[ASW]", new_name, flags=re.I)
                new_name = new_name.replace(".mkv", "")
                new_name = str(new_name + ".mkv")
                dir_name = re.sub(r"^\[ASW\] ", "", fn, flags=re.I)
                dir_name = re.sub(r" - [0-9]+ \[.*", "", dir_name, flags=re.I)
                dir_name = re.sub(r" - [0-9]+v[0-9] \[.*", "", dir_name, flags=re.I)
                dir_name = re.sub(r" - [0-9]+\.5 \[.*", "", dir_name, flags=re.I)
                dir_name = re.sub(r"\[.*\]?", "", dir_name, flags=re.I)
                dir_name = re.sub(r"\.mkv", "", dir_name, flags=re.I)
                dir_name = re.sub(r"\s+$", "", dir_name, flags=re.I)
                dir_name = re.sub(r"^\s+", "", dir_name, flags=re.I)
                new_dir = f"{basedir}/nyaa/ASW/{dir_name}"
                new = os.path.join(new_dir, new_name).replace("\\", "/")
                old = os.path.join(basedir, fn).replace("\\", "/")
                try:
                    os.makedirs(new_dir)
                    print(f"Created folder {dir_name}.")
                except FileExistsError:
                    pass
                try:
                    os.rename(old, new)
                    print(f"Moved into folder {dir_name}; {new_name}")
                except FileExistsError:
                    os.remove(old)
                    print(f"{new_name} already exists; deleting...")


def move_nyaa(path):
    for root, _, files in os.walk(path):
        for file in files:
            full_name = os.path.join(root, file).replace("\\", "/")
            new_file_name = str(full_name.replace(f"S:/crimson/fin/ASW", videos))
            new_dir_name = re.sub(r"/[^/]*$", "", new_file_name)
            try:
                os.makedirs(new_dir_name)
            except FileExistsError:
                pass
            try:
                os.rename(full_name, new_file_name)
            except FileExistsError:
                os.remove(full_name)


clear_console()

if check_file():
    create_nyaa()
    sort_nyaa()
    move_nyaa(nyaa)
else:
    print(f"\nThere were no valid files found in {basedir}\n")

