# Complexity (n = number of integers in nums)
# Time complexity: O(log(n))
# Space complexity: O(1)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = lower_bound(nums, target)
        if left == -1:
            return -1, -1
        right = upper_bound(nums, target)
        return left, right


def lower_bound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1

    if left == len(nums):
        return -1
    elif nums[left] == target:
        return left
    return -1


def upper_bound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    right_most_pos = -1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            right_most_pos = max(right_most_pos, mid)
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return right_most_pos
