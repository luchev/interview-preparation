# Complexity (n = number of items in all lists)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_num = arrays[0][0]
        max_num = arrays[0][-1]
        for i in range(1, len(arrays)):
            res = max(res, abs(arrays[i][-1] - min_num),
                      abs(max_num - arrays[i][0]))
            min_num = min(min_num, arrays[i][0])
            max_num = max(max_num, arrays[i][-1])
        return res
