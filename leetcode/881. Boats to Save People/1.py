# Complexity (n = number of items in the list)
# Time complexity: O(n * log(n))
# Space complexity: O(n) for the sorting

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) -1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
        
        return boats
