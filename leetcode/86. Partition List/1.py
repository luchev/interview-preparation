# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = ListNode()
        lessPtr = less
        greater = ListNode()
        greaterPtr = greater
        while head is not None:
            if  head.val < x:
                lessPtr.next = head
                lessPtr = head
            else:
                greaterPtr.next = head
                greaterPtr = head
            head = head.next
            
        lessPtr.next = greater.next
        greaterPtr.next = None
        return less.next