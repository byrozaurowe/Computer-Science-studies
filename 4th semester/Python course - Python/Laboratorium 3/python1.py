def transp(tab):
    return [str(k * 3 + i + 1) + '.' + tab[i].split()[k][2] for k in range(len(tab)) for i in range(len(tab))]


def main():
    tab = []
    tab = input()
    tab = transp(tab)
    print(tab)


if __name__ == "__main__":
    main()