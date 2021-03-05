def list_powerset(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result], lst, [[]])
 
def powerset(s):
    return list(map(list, list_powerset(list(s))))

def main():
    print(powerset([1, 3, 5, 7]))


if __name__ == "__main__":
    main()