# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 0:
            return []

        remaining = []
        remaining.append(asteroids[0])
        for i in range(1, len(asteroids)):
            remaining.append(asteroids[i])
            while len(remaining) >= 2:
                if remaining[-1] < 0 and remaining[-2] > 0:
                    if abs(remaining[-1]) == abs(remaining[-2]):
                        remaining.pop()
                        remaining.pop()
                    elif abs(remaining[-1]) > abs(remaining[-2]):
                        remaining.pop(-2)
                    elif abs(remaining[-1]) < abs(remaining[-2]):
                        remaining.pop(-1)
                else:
                    break
        
        return remaining
