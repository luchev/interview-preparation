# Complexity (n = length of nums)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countSubarray(upperbound):
            result = 0
            length = 0
            for x in nums:
                if x <= upperbound:
                    length += 1
                    result += length
                else:
                    length = 0
            return result
        return countSubarray(right) - countSubarray(left - 1)