# Complexity (n = length of list 1, k = length of list 2)
# Time complexity: O(n + k)
# Space complexity: O(1)

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        aLen = getLen(headA)
        bLen = getLen(headB)
        
        if aLen > bLen:
            aLen, bLen = bLen, aLen
            headA, headB = headB, headA
        
        while aLen < bLen:
            headB = headB.next
            bLen -= 1
        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None

def getLen(root: ListNode) -> int:
    length = 0
    
    while root:
        root = root.next
        length += 1
    
    return length
