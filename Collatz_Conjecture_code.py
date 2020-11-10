def collatz_Conjecture(n):
    if n / 2 == int(n / 2):
        return n / 2
    else:
        return 3 * n + 1


def function(n):
    send = -1
    if (n - 1) / 3 == int((n - 1) / 3) or (n - 1) / 3 != 0 or (n - 1) / 3 != 1:
        send = 3 * (n + 1)
    return n * 2, send


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


# Use the insert method to add nodes
root = Node(1)
root.insert(6)

root.PrintTree()
