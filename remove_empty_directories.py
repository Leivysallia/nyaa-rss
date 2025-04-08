import os

backup_drive = 'D:/'
dropbox = 'S:/Dropbox'
error_set = set([])
ess = 'S:/'
fin = 'S:/crimson/fin'
full_set = set([])
one_drive = 'S:/OneDrive'
temp = 'S:/crimson/temp'

def remove_empty_directories(root):
    for _ in range(9):
        for dirpath, dir_names, filenames in os.walk(root):
            if not filenames and not dir_names:
                if dirpath != root:
                    full_set.add(dirpath)
                    if dirpath not in error_set:
                        try:
                            os.rmdir(dirpath)
                            print(f'{dirpath} empty; removing.')
                        except PermissionError:
                            error_set.add(dirpath)
                            print(f'PermissionError; {dirpath} not removed!')
        if full_set == error_set:
            break

#remove_empty_directories(dropbox)
#remove_empty_directories(one_drive)
remove_empty_directories(fin)