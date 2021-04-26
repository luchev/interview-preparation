# Complexity (n = number of buildings)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

from typing import List
from queue import PriorityQueue

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        walls = PriorityQueue()
        for i in range(1, len(heights)):
            difference = heights[i] - heights[i-1]
            if difference < 0:
                continue
            walls.put(difference)
            if walls.qsize() <= ladders:
                continue
            bricks -= walls.get()
            if bricks < 0:
                return i - 1
        return len(heights) - 1
