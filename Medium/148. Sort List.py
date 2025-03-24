# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        p = ListNode(0,None)
        r = p
        Q = []
        if not head: return head
        while head:
            heappush(Q,head.val)
            if head.next: head = head.next
            else: break
        n = len(Q)
        for _ in range(n):
            v = heappop(Q)
            p.next = ListNode(v,None)
            p = p.next
        return r.next

        
        