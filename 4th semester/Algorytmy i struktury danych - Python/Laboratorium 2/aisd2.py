#!/usr/bin/env python
import sys
import time
import random
import matplotlib.pyplot
import numpy
import pylab


compare_num = 0
shift_num = 0


def time_decorator(func, args):
    global compare_num
    global shift_num
    compare_num = 0
    shift_num = 0
    begging = time.time()
    tab = func(*args)
    end = time.time()
    return tab, (end - begging)


def compare(comp, a, b):
    global compare_num
    global shift_num
    compare_num += 1
    if comp == ">=":
        if a > b:
            shift_num += 1
            return True
    if comp == "<=":
        if a < b:
            shift_num += 1
            return True
    else:
        return False


def insertion_sort(tab, comp):
    for i in range (1, len(tab)):
        key = tab[i]
        j = i-1
        while j >= 0 and compare(comp, key, tab[j]):
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = key

    return tab


def merge_sort(tab, comp):
    if len(tab) > 1:
        mid = len(tab) // 2
        left = tab[:mid]
        right = tab[mid:]
        merge_sort(left, comp)
        merge_sort(right, comp)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if compare(comp, left[i], right[j]):
              tab[k] = left[i]
              i += 1
            else:
                tab[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            tab[k]=right[j]
            j += 1
            k += 1

    return tab


def quick_sort(tab, comp):
    less = []
    equal = []
    greater = []

    if len(tab) > 1:
        pivot = tab[0]
        for x in tab:
            if compare(comp, x, pivot):
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif compare(comp, pivot, x):
                greater.append(x)
        return quick_sort(less, comp) + equal + quick_sort(greater, comp)  
    else: 
        return tab


def main():
    sort_type = ""
    comp = ""
    file_name = ""
    k = 0
    stat = False
    if len(sys.argv) == 5:
        if sys.argv[1] == "--type" and sys.argv[3] == "--comp":
            sort_type = sys.argv[2]
            comp = sys.argv[4]
        else:
            if sys.argv[3] == "--type" and sys.argv[1] == "--comp":
                sort_type = sys.argv[4]
                comp = sys.argv[2]
            else:
                print("Wrong format of arguments!")
                sys.exit()
    elif len(sys.argv) == 8:
        if sys.argv[1] == "--type" and sys.argv[3] == "--comp" and sys.argv[5] == "--stat":
            sort_type = sys.argv[2]
            comp = sys.argv[4]
            file_name = sys.argv[6]
            k = int(sys.argv[7])
            stat = True
        else:
            if sys.argv[3] == "--type" and sys.argv[1] == "--comp" and sys.argv[5] == "--stat":
                sort_type = sys.argv[4]
                comp = sys.argv[2]
                file_name = sys.argv[6]
                k = int(sys.argv[7])
                stat = True
            else:
                print("Wrong format of arguments!")
                sys.exit()

    else:
        print("Wrong number of arguments!")
        sys.exit()

    if stat == False:
        n = int(input())
        tab = []
        for i in range(n):
            tab.append(int(input()))

        sorted_tab = []
        if sort_type == "insert":
            sorted_tab, func_time = time_decorator(insertion_sort, [tab, comp])
        if sort_type == "merge":
            sorted_tab, func_time = time_decorator(merge_sort, [tab, comp])
        if sort_type == "quick":
            sorted_tab, func_time = time_decorator(quick_sort, [tab, comp])
        print("Czas działania algorytmu: " + str(func_time))
        print("Liczba porównań: " + str(compare_num))
        print("Liczba przestawień: " + str(shift_num))
        print(sorted_tab)

    if stat == True:
        x = [i for i in range (100, 10001, 100)]
        y1, y2, y3, y4, y5 = [], [], [], [], []
        write_file = open(file_name, "w")
        for i in range (100, 10001, 100):
            y1.append(0)
            y2.append(0)
            y3.append(0)
            ind = int(i/100 - 1)
            for j in range (k):
                tab = [random.randint(0, 10000) for l in range (i)]
                if sort_type == "insert":
                    sorted_tab, func_time = time_decorator(insertion_sort, [tab, comp])
                if sort_type == "merge":
                    sorted_tab, func_time = time_decorator(merge_sort, [tab, comp])
                if sort_type == "quick":
                    sorted_tab, func_time = time_decorator(quick_sort, [tab, comp])
                
                write_file.write("n = " + str(i) + "\n")
                write_file.write("t = " + str(func_time) + "\n")
                write_file.write("c = " + str(compare_num) + "\n")
                write_file.write("s = " + str(shift_num) + "\n")

                y1[ind] += compare_num
                y2[ind] += shift_num
                y3[ind] += func_time
            y1[ind] /= k
            y2[ind] /= k
            y3[ind] /= k
            y4.append(y1[ind] / i)
            y5.append(y2[ind] / i)
        pylab.subplot(2, 2, 1)
        pylab.plot(x, y1, 's', x, y2, 's')
        pylab.ylabel("c, s")
        pylab.xlabel("n ∈ {100,200,300, . . . ,10000}")
        pylab.grid(True)
        pylab.subplot(2, 2, 2)
        pylab.plot(x, y3, 's')
        pylab.grid(True)
        pylab.ylabel("czas")
        pylab.xlabel("n ∈ {100,200,300, . . . ,10000}")
        pylab.subplot(2, 2, 3)
        pylab.plot(x, y4, 's')
        pylab.grid(True)
        pylab.ylabel("c / n")
        pylab.xlabel("n ∈ {100,200,300, . . . ,10000}")
        pylab.subplot(2, 2, 4)
        pylab.plot(x, y5, 's')
        pylab.ylabel("s / n")
        pylab.xlabel("n ∈ {100,200,300, . . . ,10000}")
        pylab.grid(True)
        pylab.show()
        write_file.close()


if __name__ == "__main__":
    main()