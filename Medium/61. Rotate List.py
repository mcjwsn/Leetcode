# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        a = head
        cnt = 1
        while head.next:
            cnt+=1
            head = head.next
        k%=cnt
        for _ in range(k):
            p = a
            head = a
            while head.next.next:
                head = head.next
            a = head.next
            a.next = p
            head.next = None
        return a