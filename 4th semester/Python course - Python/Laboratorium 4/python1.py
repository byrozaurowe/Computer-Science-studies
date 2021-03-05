import time


def sample(a, b):
    for i in range (100000):
        a += b
    return a + b


def time_decorator(func, args):
    begging = time.time()
    sample(*args)
    end = time.time()
    return end - begging


def main():
    print(str(time_decorator(sample, [10, 5])) + " seconds")


if __name__ == "__main__":
    main()