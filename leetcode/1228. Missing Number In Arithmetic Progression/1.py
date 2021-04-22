# Complexity (n = length of input array)
# Time complexity: O(log(n))
# Space complexity: O(1)

from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        difference = (arr[-1] - arr[0]) // len(arr)
        left = 0
        right = len(arr) - 1
        while left != right:
            mid = (left + right) // 2
            if arr[0] + mid * difference == arr[mid]:
                left = mid + 1
            else:
                right = mid
        return arr[0] + right * difference
