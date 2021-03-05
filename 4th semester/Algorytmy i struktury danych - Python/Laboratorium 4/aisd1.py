import sys

class hmap():
    def __init__(self):
        self.n = 20
        self.T = [None for i in range (self.n)]

    def hash(self, data):
        #haszowanie
        h = 0
        for i in range(len(data)):
            h = 2*h + 1 - (ord(data[i]))
        h = h % self.n
        return h

    def insert(self, data):
        h = self.hash(data)
        if self.T[h] == None:
            self.T[h] = RBT()
        self.T[h].insert(data)
    
    def load(self, file):
        try:
            with open(file) as f:
                for line in f:
                    tab = line.split()
                    for word in tab:
                        if word.isalpha() == False:
                            if word[0].isalpha() == False:
                                word = word[1:len(word)]
                            if word[len(word) - 1].isalpha() == False:
                                word = word[0:(len(word) - 1)]
                        self.insert(word)
        except FileNotFoundError:
            print("file doesn't exist!")    

    def delete(self, data):
        h = self.hash(data)
        if self.T[h]:
            succ = self.T[h].successor(self.T[h].root, data)
            self.T[h].root = self.T[h].delete(data, self.T[h].root)
            if succ is not None:
                self.T[h].delete_fix(succ)

    def find(self, data):
        h = self.hash(data)
        if self.T[h]:
            self.T[h].find(self.T[h].root, data)
        return 0


class rbt_Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'R'


class RBT():
    def __init__(self):
        self.root = rbt_Node()
        self.nil = rbt_Node()
        self.nil.color = 'B'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, data):
        if self.root.data == None:
            self.root.data = data
            self.root.right = self.nil
            self.root.left = self.nil
        else:
            def add_to_root(data, root):
                if data < root.data:
                    if root.left == self.nil:
                        root.left = rbt_Node(data)
                        root.left.parent = root
                        return root.left
                    else:
                        return add_to_root(data, root.left)
                if data > root.data:
                    if root.right == self.nil:
                        root.right = rbt_Node(data)
                        root.right.parent = root
                        return root.right
                    else:
                        return add_to_root(data, root.right)
            X = add_to_root(data, self.root)
            X.right = self.nil
            X.left = self.nil

            while X != self.root and X.parent.color == 'R':
                if X.parent == X.parent.parent.right:
                    u = X.parent.parent.left
                    if u.color == 'R':
                        u.color = 'B'
                        X.parent.color = 'B'
                        X.parent.parent.color = 'R'
                        X = X.parent.parent
                    else:
                        if X == X.parent.left:
                            X = X.parent
                            self.right_rotate(X)
                        X.parent.color = 'B'
                        X.parent.parent.color = 'R'
                        self.left_rotate(X.parent.parent)
                else:
                    u = X.parent.parent.right
                    if u.color == 'R':
                        u.color = 'B'
                        X.parent.color = 'B'
                        X.parent.parent.color = 'R'
                        X = X.parent.parent
                    else:
                        if X == X.parent.right:
                            X = X.parent
                            self.left_rotate(X)
                        X.parent.color = 'B'
                        X.parent.parent.color = 'R'
                        self.right_rotate(X.parent.parent)
        self.root.color = 'B'

    def load(self, file):
        try:
            with open(file) as f:
                for line in f:
                    tab = line.split()
                    for word in tab:
                        if word.isalpha() == False:
                            if word[0].isalpha() == False:
                                word = word[1:len(word)]
                            if word[len(word) - 1].isalpha() == False:
                                word = word[0:(len(word) - 1)]
                        self.insert(word)
        except FileNotFoundError:
            print("file doesn't exist!")

    def inorder(self, node):
        if node.data != None:
            if node.left:
                self.inorder(node.left)
            print(node.data, end = " ")
            if node.right:
                self.inorder(node.right)
    
    def min_value(self, node): 
        current = node 
        while(current.left is not self.nil): 
            current = current.left  
        return current

    def max_value(self, node):
        current = node
        while(current.right is not self.nil):
            current = current.right
        return current  

    def delete(self, data, node):
        if node is self.nil or node is None:
            return node
        if data < node.data:
            node.left = self.delete(data, node.left)
        elif data > node.data:
            node.right = self.delete(data, node.right)
        else:
            if node.left is self.nil:
                temp = node.right
                node = None
                return temp
            elif node.right is self.nil:
                temp = node.left
                node = None
                return temp
            temp = self.min_value(node.right)
            node.data = temp.data
            node.right = self.delete(temp.data, node.right)
        return node

    def find(self, node, data):
        if node.data == data:
            return 1
        if node.left:
            if self.find(node.left, data) == 1:
                return 1
        if node.right:
            if self.find(node.right, data) == 1:
                return 1
        return 0
    
    def parent(self, node, target):
        if node == None:
            return False
        if node.data == target.data:
            return True
        lewy = self.parent(node.left, target)
        prawy = self.parent(node.right, target)
        if (lewy == True or  prawy == True):
            return node
        elif (type(lewy) == rbt_Node or type(prawy) == rbt_Node):
            if type(lewy) == rbt_Node:
                if lewy.data > target.data:
                    return lewy
            if type(prawy) == rbt_Node:
                if prawy.data > target.data:
                    return prawy
            return node
        else:
            return False
        

    def successor(self, node, data):
        if node.data == data:
            if node == self.root:
                return None
            if node.right is not self.nil:
                return self.min_value(node.right)
            else:
                if node == self.root:
                    return None
                else:
                    parent = self.parent(self.root, node)
                    if data < parent.data:
                        return parent
        if data < node.data:
            if node.left is not self.nil:
                return self.successor(node.left, data)
        if data > node.data:
            if node.right is not self.nil:
                return self.successor(node.right, data)
        else:
            return None

    def delete_fix(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'R':
                    s.color = 'B'
                    x.parent.color = 'R'
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 'B' and s.right.color == 'B':
                    s.color = 'R'
                    x = x.parent
                else:
                    if s.right.color == 'B':
                        s.left.color = 'B'
                        s.color = 'R'
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 'B'
                    s.right.color = 'B'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'R':
                    s.color = 'B'
                    x.parent.color = 'R'
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 'B' and s.right.color == 'B':
                    s.color = 'R'
                    x = x.parent
                else:
                    if s.left.color == 'B':
                        s.right.color = 'B'
                        s.color = 'R'
                        self.left_rotate(s)
                        s = x.parent.left 

                    s.color = x.parent.color
                    x.parent.color = 'B'
                    s.left.color = 'B'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'B'

class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    
class BST():
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        if self.root.data == None:
            self.root.data = data
        else:
            def add_to_root(data, root):
                if data < root.data:
                    if root.left == None:
                        root.left = Node(data)
                    else:
                        add_to_root(data, root.left)
                if data > root.data:
                    if root.right == None:
                        root.right = Node(data)
                    else:
                        add_to_root(data, root.right)
            add_to_root(data, self.root)

    def load(self, file):
        try:
            with open(file) as f:
                for line in f:
                    tab = line.split()
                    for word in tab:
                        if word.isalpha() == False:
                            if word[0].isalpha() == False:
                                word = word[1:len(word)]
                            if word[len(word) - 1].isalpha() == False:
                                word = word[0:(len(word) - 1)]
                        self.insert(word)
        except FileNotFoundError:
            print("file doesn't exist!")

    def inorder(self, node):
        if node.data != None:
            if node.left:
                self.inorder(node.left)
            print(node.data, end = " ")
            if node.right:
                self.inorder(node.right)
    
    def min_value(self, node): 
        current = node 
        while(current.left is not None): 
            current = current.left  
        return current

    def max_value(self, node):
        current = node
        while(current.right is not None):
            current = current.right
        return current  

    def delete(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete(data, node.left)
        elif data > node.data:
            node.right = self.delete(data, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.min_value(node.right)
            node.data = temp.data
            node.right = self.delete(temp.data, node.right)
        return node

    def find(self, node, data):
        if node.data == data:
            return 1
        if node.left:
            if self.find(node.left, data) == 1:
                return 1
        if node.right:
            if self.find(node.right, data) == 1:
                return 1
        return 0
    
    def parent(self, node, target):
        if node == None:
            return None
        if node.data == target.data:
            return True
        lewy = self.parent(node.left, target)
        prawy = self.parent(node.right, target)
        if (lewy == True or  prawy == True):
            return node
        elif (type(lewy) == Node or type(prawy) == Node):
            if type(lewy) == Node:
                if lewy.data > target.data:
                    return lewy
            if type(prawy) == Node:
                if prawy.data > target.data:
                    return prawy
            return node
        else:
            return None
        

    def successor(self, node, data):
        if node.data == data:
            if node.right:
                return self.min_value(node.right)
            else:
                if node == self.root:
                    return None
                else:
                    parent = self.parent(self.root, node)
                    if parent:
                        if data < parent.data:
                            return parent
                    else:
                        return None
        if data < node.data:
            if node.left:
                return self.successor(node.left, data)
        if data > node.data:
            if node.right:
                return self.successor(node.right, data)
        else:
            return None
    

def main():
    tree_type = ""
    n = int(input())
    if len(sys.argv) == 3:
        if (sys.argv[1] == "--type"):
            tree_type = sys.argv[2]
            tree = None
            if tree_type == "bst":
                tree = BST()
            if tree_type == "rbt":
                tree = RBT()
            if tree_type == "hmap":
                tree = hmap()

            for i in range (n):
                task = input().split()
                if task[0] == "insert":
                    if task[1].isalpha() == False:
                        if task[1][0].isalpha() == False:
                            task[1] = task[1][1:len(task[1])]
                        if task[1][len(task[1]) - 1].isalpha() == False:
                            task[1] = task[1][0:(len(task[1]) - 1)]
                    tree.insert(task[1])
                if task[0] == "load":
                    tree.load(task[1])
                if task[0] == "inorder":
                    if type(tree) != hmap:
                        tree.inorder(tree.root)
                        print("\n", end="")
                    else:
                        print("")
                if task[0] == "delete":
                    if type(tree) != hmap:
                        succ = tree.successor(tree.root, task[1])
                        tree.root = tree.delete(task[1], tree.root)
                        if type(tree) == RBT and succ is not None:
                            tree.delete_fix(succ)
                    else:
                        tree.delete(task[1])
                if task[0] == "find":
                    if type(tree) != hmap:
                        print(tree.find(tree.root, task[1]))
                    else:
                        print(tree.find(task[1]))
                if task[0] == "min":
                    min_node = None
                    if type(tree) != hmap:
                        min_node = tree.min_value(tree.root)
                    if min_node:
                        print(min_node.data)
                    else:
                        print("")
                if task[0] == "max":
                    max_node = None
                    if type(tree) != hmap:
                        max_node = tree.max_value(tree.root)
                    if max_node:
                        print(max_node.data)
                    else:
                        print("")
                if task[0] == "successor":
                    succ = None
                    if type(tree) != hmap:
                        succ = tree.successor(tree.root, task[1])
                    if succ:
                        print(succ.data)
                    else:
                        print("")

        else:
            print("wrong format of arguments")
    else:
        print("wrong number of arguments")


if __name__ == "__main__":
    main()