# Complexity (n = number of items in list 1, m = number of items in list 2)
# Time complexity: O(n + m)
# Space complexity: O(n)

import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_counter = collections.Counter(nums1)
        result = []
        for num in nums2:
            if num in num1_counter and num1_counter[num] > 0:
                result.append(num)
                num1_counter[num] -= 1

        return result
