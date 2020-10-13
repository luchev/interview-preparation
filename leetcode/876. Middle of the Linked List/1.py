# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        index = 0
        while fast is not None:
            fast = fast.next
            index += 1
            if index % 2 == 0:
                slow = slow.next
        return slow
