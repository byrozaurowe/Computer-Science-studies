def flatten(tab):
    for x in tab:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x


def main():
    tab = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
    tab = list(flatten(tab))
    print(tab)


if __name__ == "__main__":
    main()