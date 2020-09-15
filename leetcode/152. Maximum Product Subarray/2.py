# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        current_max = nums[0]
        current_min = nums[0]
        result = current_max

        for i in range(1, len(nums)):
            num = nums[i]
            new_max = max(num, current_max * num, current_min * num)
            new_min = min(num, current_max * num, current_min * num)

            current_max = new_max
            current_min = new_min
            result = max(result, current_max)

        return result
