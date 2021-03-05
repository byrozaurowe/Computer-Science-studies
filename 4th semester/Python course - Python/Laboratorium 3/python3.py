def size(file):
    sum_of_sizes = sum([int(linia.split()[len(linia.split()) - 1]) for linia in file])
    return sum_of_sizes


def main():
    print("Podaj ścieżkę do pliku: ")
    path_to_file = input()
    file = open(path_to_file)
    print(size(file))


if __name__ == "__main__":
    main()