
import os

def print_dir_path(spath):

    for schild in os.listdir(spath):
        schildpath = os.path.join(spath,schild)

        if os.path.isdir(schildpath):
            print_dir_path(schildpath)

        else:
            print(schildpath)


print_dir_path("/Users/disen.chitilapilly/Desktop/python/sample/oops_usage")
