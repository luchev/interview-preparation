# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        for i in range(len(nums)):
            result.append(nums[(i - k) % len(nums)])
        nums[::] = result
