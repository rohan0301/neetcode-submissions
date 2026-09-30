# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        cycle is there when l and r equal each other
        left moves at .next
        right moves at .next.next
        both start at root
        if right.next.next is None then there is no cycle
        '''
        if head is None or head.next is None:
            return False
        left, right = head, head
        while right is not None:
            left = left.next
            right = right.next.next if right.next is not None else None
            if left == right:
                return True
        return False