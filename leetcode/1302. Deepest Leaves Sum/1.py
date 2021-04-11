# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        frontier = []
        nextFrontier = []
        if root:
            frontier.append(root)
        
        frontierSum = 0
        lastLevelSum = 0
        while len(frontier) > 0:
            current = frontier.pop()
            frontierSum += current.val
            
            if current.left:
                nextFrontier.append(current.left)
            if current.right:
                nextFrontier.append(current.right)
            
            if len(frontier) == 0:
                frontier = nextFrontier
                nextFrontier = []
                lastLevelSum = frontierSum
                frontierSum = 0
        
        return lastLevelSum
