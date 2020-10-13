# Complexity (n = number of items in the list)
# Time complexity: O(n*log(n))
# Space complexity: O(log(n))

from typing import Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        first, second = self.splitList(head)
        first = self.sortList(first)
        second = self.sortList(second)
        return self.mergeTwoLists(first, second)

    def splitList(self, head: ListNode) -> Tuple[ListNode, ListNode]:
        slow = head
        fast = head
        index = 0
        while fast is not None:
            fast = fast.next
            index += 1
            if index % 2 == 0 and index > 2:
                slow = slow.next

        second = slow.next
        slow.next = None
        first = head
        return first, second

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode()
        mergedPointer = merged

        while l1 is not None:
            if l2 is not None and l2.val <= l1.val:
                mergedPointer.next = ListNode(l2.val)
                l2 = l2.next
            else:
                mergedPointer.next = ListNode(l1.val)
                l1 = l1.next
            mergedPointer = mergedPointer.next

        while l2 is not None:
            mergedPointer.next = ListNode(l2.val)
            l2 = l2.next
            mergedPointer = mergedPointer.next

        return merged.next
