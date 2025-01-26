# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        if not head.next: return None
        for i in range(n-1):
            fast =fast.next
        if not fast.next:
            return head.next
        while fast.next.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head