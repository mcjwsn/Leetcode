# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        while head.next.next:
            if head.next.val != 0:
                head.val+= head.next.val 
                head.next = head.next.next
            else: head = head.next
        head.next = None
        return a
                      