# Complexity (n = input array length)
# Time complexity: O(n * logn)
# Space complexity: O(1)

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)//2):
            result += nums[-i-1] - nums[i]
        return result