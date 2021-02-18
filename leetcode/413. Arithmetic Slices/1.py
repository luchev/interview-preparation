# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        A.append(math.inf)
        arithmetic_slices = 0
        
        difference = None
        current_length = 1

        for i in range(1, len(A)):
            if A[i] - A[i - 1] != difference:
                if current_length >= 3:
                    arithmetic_slices +=  (current_length - 1) * (current_length - 2) // 2
                
                current_length = 2
                difference = A[i] - A[i - 1]
            else:
                current_length += 1

        return arithmetic_slices
