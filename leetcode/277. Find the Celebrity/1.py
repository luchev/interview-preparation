# Complexity (n = number of people)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List


# def knows(a: int, b: int) -> bool:
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        
        if isCelebrity(candidate, n):
            return candidate
        return -1

def isCelebrity(x, count):
    for i in range(count):
        if i != x and knows(x, i) or not knows(i, x):
            return False
    return True
