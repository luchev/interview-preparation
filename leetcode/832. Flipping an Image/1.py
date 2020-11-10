# Complexity (n = matrix rows, m = matrix columns)
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [map(lambda x: 1 if x == 0 else 0, row[::-1]) for row in A]
