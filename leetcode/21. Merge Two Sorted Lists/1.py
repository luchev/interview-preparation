# Complexity (n = length of list 1, m = length of list 2)
# Time complexity: O(n + m)
# Space complexity: O(n + m)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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
