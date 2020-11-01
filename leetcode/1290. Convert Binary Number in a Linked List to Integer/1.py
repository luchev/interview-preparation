# Complexity (n = nodes in the linked list)
# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            result <<= 1
            result += head.val
            head = head.next
        return result
