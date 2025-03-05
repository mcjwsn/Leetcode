# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mem = 0
        prev = ListNode(0,None)
        a = prev
        while l1 or l2:
            val = (l1.val + l2.val + mem)
            mem = val // 10
            val %= 10
            prev.next = ListNode(val,None)
            prev = prev.next
            if not l1.next and not l2.next:
                if mem!=0: prev.next = ListNode(mem,None)
                break
            if l1.next and l2.next: 
                l1 = l1.next
                l2 = l2.next
                continue
            if l1.next and not l2.next:
                l1 = l1.next
                l2.next = ListNode(0,None)
                l2 = l2.next
            if l2.next and not l1.next:
                l2 = l2.next
                l1.next = ListNode(0,None)
                l1 = l1.next
        return a.next