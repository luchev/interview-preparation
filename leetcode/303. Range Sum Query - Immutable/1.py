# Complexity (n = input array size)
# Time complexity: O(n) for precomputing
# Time complexity: O(1) per request
# Space complexity: O(n)

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.pre = [0]
        for x in nums:
            self.pre.append(self.pre[-1] + x)

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)