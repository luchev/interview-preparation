# Complexity (n = nodes in the list)
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        data = []
        while head:
            data.append(head.val)
            head = head.next
        
        for index in range(len(data) // 2):
            if data[index] != data[len(data) - index - 1]:
                return False
        return True
