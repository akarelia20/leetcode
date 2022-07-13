class ListNode:
    def __init__(self,val):
        self.val= val
        self.next = None

def mergeTwoList(l1, l2):
    head = ListNode()
    tail = head

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1= l1.next
        else:
            tail.next = l2
            l2= l2.next
        tail = tail.next
    
    tail.next = l1 or l2

    return head.next


l1 = ListNode([1,2,4])
l2 = ListNode([1,3,4])

print(mergeTwoList(l1,l2))