# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append(-1)
        max_area = 0
        for index, height in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= height:
                temp_height = heights[stack.pop()]
                width = index - stack[-1] - 1
                max_area = max(max_area, temp_height * width)
            stack.append(index)
            
        while stack[-1] != -1:
            temp_height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, temp_height * width)
        
        return max_area
