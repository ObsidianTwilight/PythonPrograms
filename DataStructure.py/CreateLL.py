
class Node:
    def __init__(self,data,ref = None):
        self.data = data
        self.ref = None
    
class LinkedList:
    def __init__(self):
        self.head = None # Empty Linked list
    
    def traverse_list(self): # Traversal operation of linked list
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
LL1 = LinkedList()
LL1.traverse_list()
    


        
    

