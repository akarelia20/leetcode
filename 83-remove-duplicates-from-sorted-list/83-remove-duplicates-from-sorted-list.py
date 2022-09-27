# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current node is head node
        current = head
        while current:  # while current is not null
            # while next node exist and next node has same value as current node
            while current.next and current.next.val == current.val:
                # set next node to next to next node , meaning skip next node
                current.next = current.next.next
            # now set current to current.next
            current = current.next
        return head