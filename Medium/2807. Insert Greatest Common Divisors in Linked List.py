# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x,y):
            while True:
                if x==y or x==0 or y == 0 : return max(x,y)
                if x< y:return gcd(x,y%x)
                else: return gcd(y,x%y)
        p = head
        while head.next:
            a = ListNode(gcd(head.val, head.next.val),head.next)
            head.next = a
            head = a.next
        return p