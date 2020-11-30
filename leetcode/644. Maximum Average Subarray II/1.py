# Complexity (n = length of numbers, error = 0.00001, p = max(nums) - min(nums) / error)
# Time complexity: O(n * log(p))
# Space complexity: O(1)

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = min(nums)
        right = max(nums)
        err = abs(right - left)
        old_mid = left
        while err > 0.00001:
            mid = (left + right) / 2
            if possibleAverageSubarray(nums, mid, k):
                left = mid
            else:
                right = mid
            err = abs(mid - old_mid)
            old_mid = mid
        return left


def possibleAverageSubarray(nums, avg, interval_len):
    current_sum = sum(nums[:interval_len]) - avg * interval_len
    if current_sum >= 0:
        return True
    prev_sum = 0
    min_sum = 0
    for i in range(interval_len, len(nums)):
        current_sum += nums[i] - avg
        prev_sum += nums[i - interval_len] - avg
        min_sum = min(prev_sum, min_sum)
        if current_sum >= min_sum:
            return True
    return False
