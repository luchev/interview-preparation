# Complexity (n = matrix columns, m = matrix rows)
# Time complexity: O(n^2 * m^2)
# Space complexity: O(n)

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSum1D(arr):
            maxSubSum = -math.inf
            curSum = 0
            prefixSums = [math.inf]
            for x in arr:
                bisect.insort(prefixSums, curSum)
                curSum += x
                i = bisect.bisect_left(prefixSums, curSum - k)
                maxSubSum = max(maxSubSum, curSum - prefixSums[i])
            return maxSubSum
        
        m = len(matrix)
        n = len(matrix[0])
        
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y + 1] += matrix[x][y]
        
        result = -math.inf
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = [matrix[x][y2] - (matrix[x][y1 - 1] if y1 >= 1 else 0) for x in range(m)]
                result = max(result, maxSum1D(arr))
        return result