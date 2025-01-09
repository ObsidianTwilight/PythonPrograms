class ListNode(object):
    def __init__(self,Val = 0, Next = None):
        self.val = Val
        self.next = Next

class solution:
    def AddTwoNumbers(self, l1, l2):
        l1: ListNode
        l2: ListNode
        l3: ListNode

        carry: int = 0
        while(l1 != None or l2 != None):
            sum = sum + carry
            if l1 != None:
                sum = sum(l1.val) + carry
                l1.next = next

            if l2 != None:
                sum = sum(l1.val) + carry
                l2.next = next
            
            sum = sum % 10
            carry = sum / 10
            l3 = l1.val + l2.val
            return l3
                
            

    


        
        
        