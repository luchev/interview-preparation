from typing import List

def isPeak(nums, index):
    if index == 0:
        return nums[index] > nums[index + 1]
    if index == len(nums) - 1:
        return nums[index] > nums[index - 1]
    return nums[index] > nums[index - 1] and nums[index] > nums[index + 1]

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while not isPeak(nums, mid):
            if mid == len(nums) or nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        return mid

