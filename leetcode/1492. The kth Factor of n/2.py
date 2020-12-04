# Complexity (n = number to find factors for, k = Kth factor to find)
# Time complexity: O(sqrt(n) * log k)
# Space complexity: O(sqrt(n))

from queue import PriorityQueue
from math import sqrt, ceil
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = PriorityQueue() # min heap so we have to keep negative numbers to make it max
        for x in range(1, int(sqrt(n) + 1)):
            if n % x == 0:
                factors.put(-x)
                if x != n // x:
                    factors.put(- n//x)
        if factors.qsize() < k:
            return -1
        
        while factors.qsize() > k:
            factors.get()
        
        return -factors.get()
