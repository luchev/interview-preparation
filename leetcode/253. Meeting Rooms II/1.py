# Complexity (n = number of intervals)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
from queue import PriorityQueue

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pqueue = PriorityQueue()
        max_rooms = 0
        for inter in intervals:
            pqueue.put(inter[1])
            while pqueue.qsize() > 0 and pqueue.queue[0] <= inter[0]:
                pqueue.get()
            max_rooms = max(max_rooms, pqueue.qsize())
        return max_rooms
