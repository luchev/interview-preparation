# Complexity (n = number of items in the stack)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stak = []
        popped_index = 0
        
        for x in pushed:
            stak.append(x)
            while stak and stak[-1] == popped[popped_index]:
                stak.pop()
                popped_index += 1
        
        return popped_index == len(popped)
