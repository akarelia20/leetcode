# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        skip_one = skip_two = head
        # skip_two = skip_one
        
        while skip_two and skip_two.next:
            skip_one = skip_one.next
            skip_two= skip_two.next.next
            
        return skip_one