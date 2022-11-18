# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict = {}
        while head:
            if head in dict:
                return True
            dict[head] = True
            head = head.next
        return False
        
        