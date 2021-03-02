# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check = [False] * (len(nums) + 1)
        result = []

        for x in nums:
            if check[x] == True:
                result.append(x)
            check[x] = True

        for i in range(1, len(nums) + 1):
            if not check[i]:
                result.append(i)

        return result
