# Complexity (n = number nodes in the list)
# Time complexity: O(n^2)
# Space complexity: O(1)

import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        new_list = ListNode(-math.inf)

        while head:
            next_ptr = head.next
            self.insertInSortedList(new_list, head)
            head = next_ptr
        return new_list.next

    def insertInSortedList(self, head: ListNode, new: ListNode) -> None:
        succ = head.next
        while succ:
            if head.val <= new.val <= succ.val:
                break
            succ = succ.next
            head = head.next
        new.next = succ
        head.next = new
