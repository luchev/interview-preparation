# Complexity (n = matrix rows, m = matrix cols, k = unique numbers in matrix)
# Time complexity: O(n * m)
# Space complexity: O(k)

from typing import List
from collections import Counter
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counts = Counter(x for lis in mat for x in lis)
        try:
            return min(x for x, count in counts.items() if count == len(mat))
        except:
            return -1
