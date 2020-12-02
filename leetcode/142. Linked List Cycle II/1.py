# Complexity (n = number of nodes in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        intersection = findIntersection(head)
        if intersection is None:
            return None
        
        while head != intersection:
            head = head.next
            intersection = intersection.next
        return intersection
        
def findIntersection(head: ListNode):
    slow = head
    fast = head
    while True:
        if fast is None:
            return None
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
        if fast == slow:
            return slow
