# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n) for the recursion stack

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Going forward in the recursion we calculate the length
        # Returning from the recursion we remove the desired node
        head, length = self.removeNthFromEndRecursive(head, n, 0)

        return head

    def removeNthFromEndRecursive(self, head, n, length):
        if head is None:
            return (head, length)

        index = length
        head.next, length = self.removeNthFromEndRecursive(
            head.next, n, length + 1)
        if length - n == index:
            return head.next, length
        return head, length
