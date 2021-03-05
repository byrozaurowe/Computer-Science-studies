import random


def bfs(tree):
    new = []
    for x in tree:
        if isinstance(x, int):
            yield x
        else:
            if isinstance(x, list):
                for y in x:
                    new.append(y)
    if len(new) > 0:
        yield from bfs(new)


def dfs(tree):
    for x in tree:
        if isinstance(x, list):
            yield from dfs(x)
        else:
            if x != None:
                yield x


def generate_tree(n):
    if n == 0:
        return []
    if n == 1:
        tree = [random.randint(0, 101), None, None]
        return tree
    else:
        move = random.randint(0, 1)
        if move == 0:
            move = random.randint(0, 1)
            if move == 0:
                return [random.randint(0, 101), generate_tree(n-1), None]
            else:
                return [random.randint(0, 101), generate_tree(n-1), generate_tree(random.randint(1, n-1))]
        else:
            move = random.randint(0, 1)
            if move == 0:
                return [random.randint(0, 101), None, generate_tree(n-1)]
            else:
                return [random.randint(0, 101), generate_tree(random.randint(1, n-1)), generate_tree(n-1)]


def main():
    n = int(input())
    tree = generate_tree(n)
    print (tree)
    tree_dfs = list(dfs(tree))
    print(tree_dfs)
    tree_bfs = list(bfs(tree))
    print(tree_bfs)


if __name__ == "__main__":
    main()