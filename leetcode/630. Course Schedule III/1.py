# Complexity (n = number of courses)
# Time complexity: O(nlogn)
# Space complexity: O(n)

from typing import List
from queue import PriorityQueue

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        que = PriorityQueue()
        time = 0
        for x in courses:
            if time + x[0] <= x[1]:
                time += x[0]
                que.put(-x[0])
            elif que.qsize() > 0 and -que.queue[0] > x[0]:
                time += x[0] + que.get()
                que.put(-x[0])
        return que.qsize()