# Complexity (n = number of items in the list)
# Time complexity: O(n^2)
# Space complexity: O(n)

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        lengths = [0] * len(nums)
        counts = [1] * len(nums)

        for index, num in enumerate(nums):
            for i in range(index):
                if nums[i] < nums[index]:
                    if lengths[i] >= lengths[index]:
                        lengths[index] = 1 + lengths[i]
                        counts[index] = counts[i]
                    elif lengths[i] + 1 == lengths[index]:
                        counts[index] += counts[i]

        longest = max(lengths)
        all_counts = 0
        for i in range(len(counts)):
            if lengths[i] == longest:
                all_counts += counts[i]
        return all_counts
