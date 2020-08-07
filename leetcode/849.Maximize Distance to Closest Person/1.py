# Complexity(n = length of seats)
# Time complexity: O(n)
# Space complexity: O(1)
import math

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        bestStart = -1
        bestEnd = -1
        currentStart = -1
        currentEnd = -1
        startPieceLen = -1
        endPieceLen = -1
        midPieceLen = -1
        
        for i in range(0, len(seats)):
            if seats[i] == 1:
                currentStart = -1
                continue
            
            if currentStart == -1:
                currentStart = i
            
            currentEnd = i
            
            if currentStart == 0:
                startPieceLen = i + 1
                
            if currentEnd - currentStart >= bestEnd - bestStart:
                bestStart = currentStart
                bestEnd = currentEnd
                
        if currentEnd == len(seats) - 1:
            endPieceLen = currentEnd - currentStart + 1
        
        midPieceLen = bestEnd - bestStart + 1
        if startPieceLen > endPieceLen and startPieceLen > midPieceLen / 2:
            return startPieceLen
        elif endPieceLen > startPieceLen and endPieceLen > midPieceLen / 2:
            return endPieceLen
        else:
            return math.ceil(midPieceLen / 2)
