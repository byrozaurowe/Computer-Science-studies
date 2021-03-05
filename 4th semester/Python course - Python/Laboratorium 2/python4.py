import hashlib
import sys
import os


def find_duplicates(paths_table):
    table = []
    for file_path in paths_table:
        file_size = os.path.getsize(file_path)
        file = open(file_path, 'rb')
        input = file.read()
        hashed_input = hashlib.sha256(input).hexdigest()
        found = False
        for i in table:
            if i[0] == file_size and i[1] == hashed_input:
                i[2].append(file_path)
                found = True
                break
        if found is False:
            table.append([file_size, hashed_input, [file_path]])

    for i in table:
        if len(i[2]) > 1:
            print(i[2])
            print("---------------------------------------------------------")


def find_files(path, paths_table):
    filenames = os.listdir(path)
    for filename in filenames:
        new_path = path + "/" + filename
        if os.path.isdir(new_path):
            paths_table = find_files(new_path, paths_table)
        file_path = path + "/" + filename
        if os.path.isfile(file_path):
            paths_table.append(file_path)
    return paths_table


def main():
    path = str(sys.argv[1])
    paths_table = []
    find_duplicates(find_files(path, paths_table))


if __name__ == "__main__":
    main()
