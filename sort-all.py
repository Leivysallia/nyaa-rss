import os
import re

asw = r"^\[ASW\].*$"
basedir = "S:/crimson/fin"
nyaa = "S:/crimson/fin/nyaa/ASW"
run = "false"
videos = "S:/OneDrive/Videos"
error_set = set([])
full_set = set([])


def check_file():
    for fn in os.listdir(basedir):
        if os.path.isfile(os.path.join(basedir, fn)):
            if re.match(asw, fn, flags=re.I):
                return True


def clear_console():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def create_nyaa():
    try:
        os.makedirs(nyaa)
        print("Created folder " + nyaa)
    except FileExistsError:
        print(nyaa + " already exists; skipping creation")


def sort_nyaa():
    for fn in os.listdir(basedir):
        if os.path.isfile(os.path.join(basedir, fn)):
            if re.match(asw, fn, flags=re.I):
                new_name = re.sub(r"\[[a-z0-9]+\]", "", fn, flags=re.I)
                new_name = re.sub("^", "[ASW]", new_name, flags=re.I)
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
                new_dir = str(basedir + "/nyaa/ASW/" + dir_name)
                new = os.path.join(new_dir, new_name).replace("\\", "/")
                old = os.path.join(basedir, fn).replace("\\", "/")
                try:
                    os.makedirs(new_dir)
                    print("Created folder " + dir_name + ".")
                except FileExistsError:
                    pass
                try:
                    os.rename(old, new)
                    print("Moved into folder " + dir_name + "; " + new_name)
                except FileExistsError:
                    os.remove(old)
                    print(new_name + " already exists; deleting...")


def move_nyaa(path):
    for root, _, files in os.walk(path):
        for file in files:
            full_name = os.path.join(root, file).replace("\\", "/")
            new_file_name = str(full_name.replace("S:/crimson/fin", videos))
            new_dir_name = re.sub(r"/[^/]*$", "", new_file_name)
            try:
                os.makedirs(new_dir_name)
            except FileExistsError:
                pass
            try:
                os.rename(full_name, new_file_name)
            except FileExistsError:
                os.remove(full_name)


def remove_empty_directories(root):
    for _ in range(9):
        for dirpath, dir_names, filenames in os.walk(root):
            if not filenames and not dir_names:
                if dirpath != root:
                    full_set.add(dirpath)
                    if dirpath not in error_set:
                        try:
                            os.rmdir(dirpath)
                            print(dirpath + " empty; removing.")
                        except PermissionError:
                            error_set.add(dirpath)
                            print("PermissionError; " + dirpath + " not removed!")
        if full_set == error_set:
            break


if check_file():
    clear_console()
    create_nyaa()
    sort_nyaa()
    move_nyaa("S:/crimson/fin/nyaa")
    remove_empty_directories(basedir)
