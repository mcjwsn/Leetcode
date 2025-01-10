# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from heapq import heappop, heappush
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Q = []
        for i in range(len(lists)):
            head = lists[i]
            if not head: continue
            while head.next:
                heappush(Q,head.val)
                head = head.next
            heappush(Q,head.val)
        if Q:
            start = heappop(Q)
        else: return 
        start = ListNode(start,None)
        prev = start
        while len(Q)>0:
            x = ListNode(heappop(Q),None)
            prev.next = x
            prev = prev.next
        return start