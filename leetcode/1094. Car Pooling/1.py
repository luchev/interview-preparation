# Complexity (n = number of trips)
# Time complexity: O(nlogn)
# Space complexity: O(n)

from typing import List
from queue import PriorityQueue

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort by start point
        trips.sort(key=lambda x: x[1])
        # restructure for the priority queue so the end point is first
        trips = [(end, start, passengers) for passengers, start, end in trips]
        pque = PriorityQueue()

        current_passengers = 0
        for end, start, people in trips:
            while pque.qsize() > 0:
                top = pque.get()
                if top[0] > start:
                    pque.put(top)
                    break
                current_passengers -= top[2]
            pque.put((end, start, people))

            current_passengers += people
            if current_passengers > capacity:
                return False

        return True
