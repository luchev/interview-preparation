# Complexity (n = length of A = length of B)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

from typing import List
from queue import PriorityQueue

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        aPQ = PriorityQueue()
        for index, val in enumerate(A):
            aPQ.put(-val)
        
        bPQ = PriorityQueue()
        for index, val in enumerate(B):
            bPQ.put((-val, index))

        order = [-1] * len(A)
        
        while not bPQ.empty():
            bTop = bPQ.get()
            aTop = aPQ.queue[0]
            if aTop < bTop[0]:
                order[bTop[1]] = -aTop
                aPQ.get()
            
        emptyIndex = 0
        for x in aPQ.queue:
            while order[emptyIndex] != -1:
                emptyIndex += 1
            order[emptyIndex] = -x
    
        return order
