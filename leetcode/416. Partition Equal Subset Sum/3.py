# Complexity (n = numbers in he input list, m = sum of all numbers / 2)
# Time complexity: O(n * m)
# Space complexity: O(m)

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total >> 1 << 1 != total:
            return False
        half = total // 2
        if max(nums) > half:
            return False

        previous_row = [False] * (half+1)
        previous_row[0] = True
        current_row = [False] * (half+1)
        current_row[0] = True

        for row in range(1, len(nums) + 1):
            for col in range(1, half + 1):
                x = nums[row - 1]
                current_row[col] = previous_row[col]
                if col - x >= 0:
                    current_row[col] |= previous_row[col - x]
            previous_row = current_row
            current_row = [False] * (half+1)
            current_row[0] = True

        return previous_row[-1]
