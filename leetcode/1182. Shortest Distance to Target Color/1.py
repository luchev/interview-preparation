# Complexity (n = length of colors, k = length of queries)
# Time complexity: O(n + k)
# Space complexity: O(n)
# O(n) for precomputing and then O(1) for each query

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        left = [[math.inf] * 4 for _ in range(len(colors))]
        left[0][colors[0]] = 0
        for i in range(1, len(colors)):
            for k in range(4):
                left[i][k] = left[i-1][k] + 1
            left[i][colors[i]] = 0
        
        right = [[math.inf] * 4 for _ in range(len(colors))]
        right[-1][colors[-1]] = 0
        for i in reversed(range(0, len(colors) - 1)):
            for k in range(4):
                right[i][k] = right[i+1][k] + 1
            right[i][colors[i]] = 0
        
        result = []
        for index, color in queries:
            result.append(min(right[index][color], left[index][color]))
            if result[-1] == math.inf:
                result[-1] = -1
        return result