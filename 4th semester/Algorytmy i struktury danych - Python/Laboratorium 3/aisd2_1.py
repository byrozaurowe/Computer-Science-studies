import sys
import random


swap_counter = 0
comp_counter = 0


def swap(tab, left, right):
    global swap_counter 
    swap_counter += 1
    tmp = tab[left]
    tab[left] = tab[right]
    tab[right] = tmp


def partition(tab, left, right):
    global comp_counter 
    x = tab[right]
    i = left
    for j in range(left, right):
        comp_counter += 1
        if tab[j] <= x:
            swap(tab, i, j)
            i += 1
    swap(tab, i, right)
    return i


def select(tab, left, right, k):
    if (right-left+1) < k:
        return
    if left == right and k == 1:
        return tab[left]
    pivot = partition(tab, left, right)
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
        comp_counter += 1
        if tab[j] <= x:
            swap(tab, i, j)
            i += 1
    swap(tab, i, right)
    return i


def randomized_select(tab, left, right, k):
    if (right-left+1) < k:
        return
    if left == right and k == 1:
        return tab[left]
    pivot = randomized_partition(tab, left, right)
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

        sel_comp = []
        rand_comp = []

        for l in range(10000):
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
                out = select(tab, 0, n - 1, k)
                sel_comp.append(comp_counter)

                comp_counter = 0
                swap_counter = 0
                out = randomized_select(tab_copy, 0, n - 1, k)
                rand_comp.append(comp_counter)

            else:
                print("Wrong format of parameter!")

        print("SELECT liczba porównań")
        print("średnia: " + str(sum(sel_comp) / len(sel_comp)) + " min: " + str(min(sel_comp)) + " max: " + str(max(sel_comp)))
        odchyl = 0
        srednia = sum(sel_comp) / len(sel_comp)
        for i in sel_comp:
            odchyl += (i-srednia)**2
            odchyl /= len(sel_comp)
        odchyl **= 0.5
        odchyl = odchyl / len(sel_comp)
        print("odchylenie standardowe: " + str(odchyl))

        print("RANDOMIZED SELECT liczba porównań")
        print("średnia: " + str(sum(rand_comp) / len(rand_comp)) + " min: " + str(min(rand_comp)) + " max: " + str(max(rand_comp)))
        odchyl = 0
        srednia = sum(rand_comp) / len(rand_comp)
        for i in rand_comp:
            odchyl += (i-srednia)**2
            odchyl /= len(rand_comp)
        odchyl **= 0.5
        odchyl = odchyl / len(rand_comp)
        print("odchylenie standardowe: " + str(odchyl))


if __name__ == "__main__":
    main()