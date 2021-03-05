import sys
import time


compare_num = 0

def time_decorator(func, args):
    begging = time.time()
    tab = func(*args)
    end = time.time()
    print("Czas działania algorytmu: " + str(end - begging))
    print("Liczba porównań: " + str(compare_num))
    return tab


def compare(comp, a, b):
    global compare_num
    compare_num += 1
    if comp == ">=":
        if a > b:
            return True
    if comp == "<=":
        if a < b:
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
    else:
        print("Wrong number of arguments!")
        sys.exit()

    n = int(input())
    tab = []
    for i in range(n):
        tab.append(int(input()))

    sorted_tab = []
    if sort_type == "insert":
        sorted_tab = time_decorator(insertion_sort, [tab, comp])
    if sort_type == "merge":
        sorted_tab = time_decorator(merge_sort, [tab, comp])
    if sort_type == "quick":
        sorted_tab = time_decorator(quick_sort, [tab, comp])

    print(sorted_tab)

if __name__ == "__main__":
    main()