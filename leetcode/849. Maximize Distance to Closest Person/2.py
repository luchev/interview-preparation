# Complexity(n = length of seats)
# Time complexity: O(n)
# Space complexity: O(1)

import math
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        bestStart = -1
        bestEnd = -1
        currentStart = -1
        currentEnd = -1
        startPieceLen = -1
        
        for i in range(0, len(seats)):
            if seats[i] == 1:
                currentStart = -1
                continue
            
            if currentStart == -1:
                currentStart = i
            
            currentEnd = i
            
            if currentStart == 0:
                startPieceLen = i + 1
                
            if currentEnd - currentStart > bestEnd - bestStart:
                bestStart = currentStart
                bestEnd = currentEnd
            
        endPieceLen = -1
        if currentEnd == len(seats) - 1:
            endPieceLen = currentEnd - currentStart + 1
        
        midPieceLen = math.ceil((bestEnd - bestStart + 1) / 2)
        
        return max(startPieceLen, endPieceLen, midPieceLen)
