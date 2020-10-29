# Complexity(n = length of seats)
# Time complexity: O(n)
# Space complexity: O(1)

import math
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        startPieceLen = 0
        startPieceDone = False
        currentLen = 0
        maxLen = 0

        for i in range(0, len(seats)):
            if seats[i] == 1:
                if currentLen > maxLen:
                    maxLen = currentLen
                startPieceDone = True
                currentLen = 0
                continue

            if not startPieceDone:
                startPieceLen += 1

            currentLen += 1

        endPieceLen = -1
        if currentLen > 0:
            endPieceLen = currentLen
        
        midPieceLen = math.ceil(maxLen / 2)

        return max(startPieceLen, endPieceLen, midPieceLen)
