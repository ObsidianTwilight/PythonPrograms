class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end = " ")
                n = n.ref
                
    def add_begin(self,data): #Must mention data
        newnode = Node(data)
        # newnode = LinkedList()
        newnode.ref = self.head
        self.head = newnode

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(200)
LL1.traverse_list()
        