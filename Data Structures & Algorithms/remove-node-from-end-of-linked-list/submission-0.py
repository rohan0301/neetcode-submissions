# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        last = head
        countl = 1
        while last.next is not None:
            last = last.next
            countl += 1
        countf = 1
        dummy = ListNode(0,head)
        prev = dummy
        for i in range(countl - n):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next
        