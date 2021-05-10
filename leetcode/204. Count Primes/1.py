# Complexity (n = input argument)
# Time complexity: O(n * log(log(n)))
# Space complexity: O(n)

import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        for i in range(2, math.ceil(len(primes) ** 0.5)):
            if not primes[i]:
                continue
            
            for k in range(i ** 2, len(primes), i):
                primes[k] = False
        
        return sum(primes)
