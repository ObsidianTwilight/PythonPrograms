from rich import print

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList(Node):
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " ", "-->", end = " ")
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
            print("node is not present in Linked list")
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            
            
            


print("This is the first Linked list")
LL1 = LinkedList()
LL1.add_begin(23)
LL1.add_begin(34)
LL1.add_begin(45)
LL1.printLL()

