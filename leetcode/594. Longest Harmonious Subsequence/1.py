# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

import collections

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count_dict = collections.Counter(nums)
        maxLen = 0

        for num in count_dict:
            if num + 1 in count_dict:
                maxLen = max(maxLen, count_dict[num] + count_dict[num + 1])

        return maxLen
