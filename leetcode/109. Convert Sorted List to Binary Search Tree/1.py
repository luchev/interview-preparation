# Complexity (n = length of linked list)
# Time complexity: O(n)
# Space complexity: O(log(n))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = listLength(head)
        
        def dfs(left, right):
            nonlocal head
            if left > right:
                return None
            mid = (left + right) // 2
            leftNode = dfs(left, mid - 1)
            current = TreeNode(head.val, leftNode)
            head = head.next
            current.right = dfs(mid + 1, right)
            return current

        return dfs(0, size - 1)
        

def listLength(head: ListNode) -> int:
    nodes = 0
    while head is not None:
        head = head.next
        nodes += 1
    return nodes
