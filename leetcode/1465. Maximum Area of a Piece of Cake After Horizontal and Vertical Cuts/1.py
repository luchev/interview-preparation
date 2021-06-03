# Complexity (n = number of horizontal cuts, k = number of vertical cuts)
# Time complexity: O(1)
# Space complexity: O(n * log(n) + k + log(k))

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontal = max(y - x for x, y in zip([0] + horizontalCuts, horizontalCuts + [h]))
        vertical = max(y - x for x, y in zip([0] + verticalCuts, verticalCuts + [w]))
        
        return (horizontal * vertical) % (10**9 + 7)