# Complexity (n = number of lists, m = total number of items in all lists)
# Time complexity: O( m * log n )
# Space complexity: O(1)
# Using merge-sort's merging strategy to merge lists recursively
# gives us a very good complexity, in theory at least
# but this approach times out

import queue
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        que = queue.SimpleQueue()
        for list_ in lists:
            que.put(list_)

        while que.qsize() >= 2:
            list1 = que.get()
            list2 = que.get()
            que.put(self.mergeTwoLists(list1, list2))

        return que.get()

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
