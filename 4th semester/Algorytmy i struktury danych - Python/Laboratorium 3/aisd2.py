import sys
import random


swap_counter = 0
comp_counter = 0


def swap(tab, left, right):
    global swap_counter 
    swap_counter += 1
    print("przestawienie:" + str(tab[left]) + " i " + str(tab[right]))
    tmp = tab[left]
    tab[left] = tab[right]
    tab[right] = tmp


def partition(tab, left, right):
    global comp_counter 
    x = tab[right]
    i = left
    for j in range(left, right):
        print("porównanie: " + str(tab[j])+ " i " + str(x))
        comp_counter += 1
        if tab[j] <= x:
            swap(tab, i, j)
            i += 1
    swap(tab, i, right)
    return i


def select(tab, left, right, k):
    print("\nstan tablicy:" + str(tab))
    if (right-left+1) < k:
        print("Wrong k size!")
        return
    if left == right and k == 1:
        return tab[left]
    pivot = partition(tab, left, right)
    print("pivot: " + str(pivot))
    k2 = pivot - left + 1
    if k == k2:
        return tab[pivot]
    elif k < k2:
        return select(tab, left, pivot - 1, k)
    else:
        return select(tab, pivot + 1, right, k - k2)


def randomized_partition(tab, left, right):
    global comp_counter 
    ind = random.randint(left, right)
    x = tab[ind]
    swap(tab, right, ind)
    i = left
    for j in range(left, right):
        print("porównanie: " + str(tab[j])+ " i " + str(x))
        comp_counter += 1
        if tab[j] <= x:
            swap(tab, i, j)
            i += 1
    swap(tab, i, right)
    return i


def randomized_select(tab, left, right, k):
    print("\nstan tablicy:" + str(tab))
    if (right-left+1) < k:
        print("Wrong k size!")
        return
    if left == right and k == 1:
        return tab[left]
    pivot = randomized_partition(tab, left, right)
    print("pivot: " + str(pivot))
    k2 = pivot - left + 1
    if k == k2:
        return tab[pivot]
    elif k < k2:
        return randomized_select(tab, left, pivot - 1, k)
    else:
        return randomized_select(tab, pivot + 1, right, k - k2)


def main():
    param = ""
    if len(sys.argv) == 2:
        param = sys.argv[1]

        print("n = ")
        n = int(input())
        print("k = ")
        k = int(input())

        tab = []
        if param == "-r" or param == "-p":
            if param == "-r":
                tab = [random.randint(0, 1000) for i in range(n)]
            elif param == "-p":
                tab = [i + 1 for i in range(n)]
                random.shuffle(tab)
            global comp_counter
            global swap_counter
            tab_copy = tab
            print("\nSELECT")
            out = select(tab, 0, n - 1, k)
            print("liczba porównań: " + str(comp_counter))
            print("liczba przestawień: " + str(swap_counter))

            for j in range(n):
                if tab[j] == out:
                    sys.stdout.write("[" + str(out) + "] ")
                else:
                    sys.stdout.write(str(tab[j]) + " ")
            print("")

            comp_counter = 0
            swap_counter = 0
            print("\nRANDOMIZED SELECT")
            out = randomized_select(tab_copy, 0, n - 1, k)
            print("liczba porównań: " + str(comp_counter))
            print("liczba przestawień: " + str(swap_counter))

            for j in range(n):
                if tab[j] == out:
                    sys.stdout.write("[" + str(out) + "] ")
                else:
                    sys.stdout.write(str(tab[j]) + " ")
            print("")

        else:
            print("Wrong format of parameter!")
    else:
        print("Wrong number of parameters!")


if __name__ == "__main__":
    main()