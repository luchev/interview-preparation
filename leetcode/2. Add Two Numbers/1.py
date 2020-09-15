# Complexity(n=max(size of list1, size of list2))
# Time complexity: O(n)
# Space complexity: O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        pointer = result
        carry = False
        while l1 or l2:
            pointer.next = ListNode()
            pointer = pointer.next
            if l1:
                pointer.val += l1.val
                l1 = l1.next
            if l2:
                pointer.val += l2.val
                l2 = l2.next
            if carry:
                pointer.val += 1
                carry = False
            if pointer.val >= 10:
                pointer.val -= 10
                carry = True
        if carry:
            pointer.next = ListNode(1)

        return result.next
