# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create dummy to handle lists with 1 element and removal of the first element
        head = ListNode(0, head)
        fast = head
        for _ in range(0, n):
            fast = fast.next

        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head.next
