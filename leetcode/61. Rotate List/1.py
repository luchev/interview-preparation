# Complexity (n = list length)
# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Nothing to do in this case
        if head is None:
            return None

        # Find the tail element
        size = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            size += 1

        # Make sure we're not doing any meaningless rotations
        k = k % size
        if k == size or k == 0 or size == 1:
            return head

        # Find the new tail
        new_tail = head
        for _ in range(size - k - 1):
            new_tail = new_tail.next

        # Redirect the pointers after we have the new head and tail
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
