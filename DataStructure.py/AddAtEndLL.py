class Node:
    def __init__(self, data):
        self.data = data 
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while self.head is not None:
                print(n.data, "-->", end = " ")
                n = n.ref

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:       # Check list is empty or not
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None: # Traverse till the end
                n = n.ref
            n.ref = new_node
            

