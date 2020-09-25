# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Comparator(str):
    def __lt__(a: str, b: str) -> bool:
        return a + b > b + a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return '0'

        str_nums = [str(x) for x in nums]
        str_nums.sort(key=Comparator)
        if str_nums[0] == '0':
            return '0'

        return ''.join(str_nums)
