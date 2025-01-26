# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = head
        n = 1
        while p.next:
            n+=1
            p = p.next
        T = [0] * (n//2)
        cnt = 0
        Flag = False
        while head.next:
            if cnt<n//2 and not Flag:
                T[cnt]+=head.val
                cnt+=1
            else:
                Flag = True
                cnt-=1
                T[cnt]+=head.val
            head = head.next
        T[0]+=head.val
        return max(T)