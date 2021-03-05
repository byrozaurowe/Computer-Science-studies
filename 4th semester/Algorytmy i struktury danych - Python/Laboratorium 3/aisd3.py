import time
import random


compare_num = 0


def time_decorator(func, args):
    global compare_num
    compare_num = 0
    begging = time.time()
    tab = func(*args)
    end = time.time()
    return tab, (end - begging)


def binary_search (arr, l, r, x): 
    global compare_num
    if r >= l: 
        mid = l + (r - l)//2
        if arr[mid] == x: 
            compare_num += 1
            return 1
        elif arr[mid] > x: 
            compare_num += 1
            return binary_search(arr, l, mid-1, x) 
        else: 
            return binary_search(arr, mid+1, r, x) 
    else: 
        return 0

    
def main():
    """print("n: ")
    n = int(input())
    print("sorted tab: ") 
    for i in range(n):
    tab.append(int(input()))
    print("v: ")
    v = int(input())"""
    for j in range(1000, 100001, 1000):
        compare_sum = 0
        time_sum = 0
        for k in range(1000):
            tab = [random.randint(0, 1000000) for k in range(j)]
            v = random.randint(0, 1000000)
            out, time = time_decorator(binary_search, [tab, 0, len(tab) - 1, v])
            time_sum += time
            compare_sum += compare_num
        print("n = " + str(j) + ": " + "średnia liczba porównań: " + str(compare_sum / 1000) + " średni czas wykonania: " + str(time_sum / 1000))


if __name__ == "__main__":
    main()