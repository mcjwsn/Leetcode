# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        if not p or not p.next: return head
        if not p.next.next:
            a = p.next
            p.next = None
            a.next = p
            return a
        a = p.next
        p.next = p.next.next
        a.next = p
        head = a
        while p.next and p.next.next:
            b = p.next
            p.next = p.next.next
            c = p.next.next
            p.next.next= b
            p.next.next.next = c
            p = p.next.next
        return head