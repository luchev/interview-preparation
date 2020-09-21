# Complexity (n = number of trips)
# Time complexity: O(max(n, 1001))
# Space complexity: O(1001)
# We can use bucket sort approach because the trips have this property:
# 0 <= start <= end <= 1000

from typing import List
from queue import PriorityQueue

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        for people, start, end in trips:
            stops[start] += people
            stops[end] -= people

        current_passengers = 0
        for stop in stops:
            current_passengers += stop
            if current_passengers > capacity:
                return False
        return True
