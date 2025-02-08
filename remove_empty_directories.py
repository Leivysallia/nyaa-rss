import os

temp = 'S:/crimson/temp'
fin = 'S:/crimson/fin'
one_drive = 'S:/OneDrive'
ess = 'S:/'

error_set = set([])
full_set = set([])

def remove_empty_directories(root):
    for _ in range(9):
        for dirpath, dir_names, filenames in os.walk(root):
            if not filenames and not dir_names:
                if dirpath != root:
                    full_set.add(dirpath)
                    if dirpath not in error_set:
                        try:
                            os.rmdir(dirpath)
                            print(dirpath + ' empty; removing.')
                        except PermissionError:
                            error_set.add(dirpath)
                            print('PermissionError; ' + dirpath + ' not removed!')
        if full_set == error_set:
            break

remove_empty_directories(fin)