import operator

def sort(array=[2, 1, 10, 16, 28, 1, 2, 0, 9, 8, 7]):
    if len(array) > 1:
        pivot = array[0]
        return sort(filter(lambda x: operator.lt(x, pivot), array))+ filter(lambda x: operator.eq(x, pivot), array) + sort(filter(lambda x: operator.gt(x, pivot), array))
    else:
        return array


def main():
    print(sort())


if __name__ == "__main__":
    main()