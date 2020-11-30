# Complexity (n = number of buildings)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

from typing import List
from queue import PriorityQueue

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = [(start, height, -1, index)
                  for index, (start, _, height) in enumerate(buildings)]
        points += [(end, height, 1, index)
                   for index, (_, end, height) in enumerate(buildings)]
        points.sort(key=lambda x: (x[0], x[1] * x[2]))

        result = []  # (x, height)
        current_buildings = set()  # index
        current_heights = PriorityQueue()  # (-height, index, x)

        for x, height, start, index in points:
            if start == -1:
                current_buildings.add(index)
            else:
                current_buildings.remove(index)

            if start == -1:
                if current_heights.qsize() == 0 or height > -current_heights.queue[0][0]:
                    result.append([x, height])
                current_heights.put((-height, index, x))
            else:
                if height == -current_heights.queue[0][0]:
                    while current_heights.qsize() > 0 and current_heights.queue[0][1] not in current_buildings:
                        current_heights.get()

                if current_heights.qsize() == 0:
                    result.append([x, 0])
                elif result[-1][1] != -current_heights.queue[0][0]:
                    result.append([x, -current_heights.queue[0][0]])

        return result
