# Complexity (n = length of list 1, m = length of list 2)
# Time complexity: O(n + m)
# Space complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1r = self.reverseList(l1)
        l2r = self.reverseList(l2)
        return self.reverseList(self.addLists(l1r, l2r))

    def addLists(self, l1: ListNode, l2: ListNode):
        ptr = ListNode()
        ans = ptr
        carry = 0
        while l1 or l2 or carry != 0:
            ptr.next = ListNode()
            ptr = ptr.next
            ptr.val += carry
            carry = 0
            if l1:
                ptr.val += l1.val
                l1 = l1.next
            if l2:
                ptr.val += l2.val
                l2 = l2.next
            if ptr.val >= 10:
                ptr.val -= 10
                carry = 1
        return ans.next

    def reverseList(self, head: ListNode) -> ListNode:
        pred = None
        # 1 -> 2 -> 3 -> 4
        while head:
            succ = head.next
            head.next = pred
            pred = head
            head = succ
        return pred
