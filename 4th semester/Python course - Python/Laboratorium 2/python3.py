import os
import sys


def rename_dir(path):
    filenames = os.listdir(path)
    for filename in filenames:
        new_path = path + "/" + filename
        if os.path.isdir(new_path):
            rename_dir(new_path)
        os.rename(path + "/" + filename, path + "/" + filename.lower())


def main():
    path = str(sys.argv[1])
    rename_dir(path)


if __name__ == "__main__":
    main()
