# Complexity (n = size of array 1, m = size of array 2)
# Time complexity: O(n + m)
# Space complexity: O(1)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m - 1
        right = n - 1
        sorted_index = m + n - 1
        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[sorted_index] = nums1[left]
                left -= 1
            else:
                nums1[sorted_index] = nums2[right]
                right -= 1
            sorted_index -= 1
        
        while left >= 0:
            nums1[sorted_index] = nums1[left]
            left -= 1
            sorted_index -= 1
        
        while right >= 0:
            nums1[sorted_index] = nums2[right]
            right -= 1
            sorted_index -= 1
