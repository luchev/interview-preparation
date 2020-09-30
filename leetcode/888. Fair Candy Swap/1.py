# Complexity (n = integers in list A, m = integers in list B)
# Time complexity: O(n + m)
# Space complexity: O(n)

from typing import List

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        compliment = (sum(A) - sum(B)) >> 1

        alice_set = set(A)
        for bob_candy in B:
            if bob_candy + compliment in alice_set:
                return [bob_candy + compliment, bob_candy]

        return [-1, -1]
