# Focused on Traversing operation

from rich import print

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList(Node):
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

N1 = Node(10)
print(N1)