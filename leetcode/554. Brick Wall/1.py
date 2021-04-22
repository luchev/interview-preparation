# Complexity (n = number of bricks)
# Time complexity: O(n * log n)
# Space complexity: O(n)

from queue import PriorityQueue
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        que = PriorityQueue()
        for row in wall:
            start = 0
            for width in row:
                que.put((start, 1)) # leftPosition, isStart
                que.put((start + width, 0)) # rightPosition, isStart
                start += width

        for _ in range(len(wall)): # remove the start of each row
            que.get()
        fewestBricks = len(wall)
        currentBricks = len(wall)
        while que.qsize() > len(wall): # while we're not at the end of the wall
            x, isStart = que.get()
            if isStart:
                currentBricks += 1
            else:
                currentBricks -= 1
                fewestBricks = min(fewestBricks, currentBricks)
        
        return fewestBricks
