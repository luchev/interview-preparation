# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sorted_list_head = ListNode(None)
        sorted_list = sorted_list_head
        prev_number = None

        while head is not None:
            if head.val != sorted_list.val and head.val != prev_number and (head.next is None or head.next.val != head.val):
                sorted_list.next = head
                sorted_list = sorted_list.next

            prev_number = head.val
            head = head.next
            
        sorted_list.next = None
        return sorted_list_head.next
