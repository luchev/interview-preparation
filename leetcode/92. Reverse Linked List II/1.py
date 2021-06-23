# Complexity (n = list length)
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummyHead = ListNode(0, head)
        beforeLeft = dummyHead
        for _ in range(left - 1):
            beforeLeft = beforeLeft.next
        last = beforeLeft.next
        
        cur = last
        curNext = last.next
        for _ in range(right - left):
            curNextNext = curNext.next
            curNext.next = cur
            cur = curNext
            curNext = curNextNext
            last.next = curNext
        
        beforeLeft.next = cur
        return dummyHead.next