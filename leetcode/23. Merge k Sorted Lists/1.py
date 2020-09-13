# Complexity (n = number of lists, m = total number of items in all lists)
# Time complexity: O( m * log(m) )
# Space complexity: O(m)
# We sacrifice some memory to gain speed because array operations are much faster than list operations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr = []
        for pointer in lists:
            while pointer is not None:
                arr.append(pointer.val)
                pointer = pointer.next

        arr.sort()

        merged = ListNode()
        mergedPointer = merged
        for item in arr:
            mergedPointer.next = ListNode(item)
            mergedPointer = mergedPointer.next

        return merged.next
