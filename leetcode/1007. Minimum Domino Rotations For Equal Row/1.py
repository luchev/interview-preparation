# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        counts = [a_i + b_i for a_i, b_i in zip(count(A), count(B))]
        d_val = counts.index(max(counts))
        if counts[d_val] < n:
            return -1

        swaps_a = 0
        swaps_b = 0
        for i in range(n):
            if A[i] != d_val and B[i] == d_val:
                swaps_a += 1
            if B[i] != d_val and A[i] == d_val:
                swaps_b += 1
            if A[i] != d_val and B[i] != d_val:
                return -1
        return min(swaps_a, swaps_b)


def count(nums: List[int]) -> List[int]:
    counter = [0] * 7
    for i in nums:
        counter[i] += 1
    return counter
