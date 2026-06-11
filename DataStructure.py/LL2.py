# Adding element at the beginning of the linked list

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

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.print_linked_list()