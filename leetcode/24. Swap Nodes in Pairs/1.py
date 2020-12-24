# Complexity (n = number of nodes in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        sentinel = ListNode(None, head)
        current = sentinel
        while current.next is not None and current.next.next is not None:
            plus_one = current.next
            current.next = current.next.next
            plus_one.next = current.next.next
            current.next.next = plus_one

            current = plus_one

        return sentinel.next
