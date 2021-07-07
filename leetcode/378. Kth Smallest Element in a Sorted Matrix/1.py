# Complexity (n = matrix rows, m = matrix columns, k = kth smallest element)
# Time complexity: O(n * log(k))
# Space complexity: O(n * m)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = functools.reduce(lambda acc, x: acc + x, matrix, [])
        heapq.heapify(arr)
        result = 0
        for _ in range(k):
            result = heapq.heappop(arr)
        return result