import random
import sys


class Node(object):
    value = 0
    left = None
    right = None


    def generate_tree(self, n):
        if n == 0:
            return None
        self.value = random.randint(0, 101)
        if n == 1:
            return 
        else:
            move = random.randint(0, 1)
            if move == 0:
                self.left = Node()
                self.left.generate_tree(n-1)
                move = random.randint(0, 1)
                if move == 0:
                    self.right = Node()
                    self.right.generate_tree(random.randint(1, n-1))
            else:
                self.right = Node()
                self.right.generate_tree(n-1)
                move = random.randint(0, 1)
                if move == 0:
                    self.left = Node()
                    self.left.generate_tree(random.randint(1, n-1))


    '''def print_tree(self):
        sys.stdout.write(str(self.value) + ', ')
        if self.left != None:
            sys.stdout.write('[')
            self.left.print_tree()
        else:
            sys.stdout.write('[None, ')
        if self.right != None:
            self.right.print_tree()
            sys.stdout.write('], ')
        else:
            sys.stdout.write('None], ') '''


    def dfs(self):
        yield self.value
        if self.left != None:
            yield from self.left.dfs()
        if self.right != None:
            yield from self.right.dfs()


    def bfs(self):
        q = [self]
        while q:
            n = q.pop(0)
            yield n.value
            if n.left != None:
                q.append(n.left)
            if n.right != None:
                q.append(n.right)
        

'''def main():
    first = Node()
    first.generate_tree(4)
    first.print_tree()
    print()
    print(list(first.dfs()))
    print(list(first.bfs()))


if __name__ == "__main__":
    main() '''