# Complexity (n = input size)
# Time complexity: O(log(n))
# Space complexity: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left