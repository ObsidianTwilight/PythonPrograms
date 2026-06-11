# Inseting/Adding elements at the end of the linked list
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
                print(n.data, "-->", end = " ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if x == self.head.data:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return



print("this is first linked list")
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(100)
LL1.add_end(200)
LL1.print_linked_list()
print("\n")
print("This linked list is for echecking for 'add_end' function works properly when LL is empty")
LL2 = LinkedList()
LL2.add_end(300)
LL2.print_linked_list()

print("\n")
print("Checking for Addition of node in between the nodes:")
LL3 = LinkedList()
LL3.add_begin(20)
LL3.add_end(40)
LL3.add_after(60, 20)
LL3.print_linked_list()