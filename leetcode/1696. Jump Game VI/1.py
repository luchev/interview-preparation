# Complexity (n = input list size, k = max jump)
# Time complexity: O(n * log(k))
# Space complexity: O(n)

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = []
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        heapq.heappush(heap, (-nums[-1], len(nums) - 1))
        for i in reversed(range(len(nums) - 1)):
            while heap[0][1] > i + k:
                heapq.heappop(heap)
            dp[i] = nums[i] + (-heap[0][0])
            heappush(heap, (-dp[i], i))
        return dp[0]