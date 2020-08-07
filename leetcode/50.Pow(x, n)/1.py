# Complexity(n = power)
# Time complexity: O(logn)
# Space complexity: O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x * x
        elif n < 0:
            return 1 / self.myPow(x, -n)
        
        if ((n >> 1) << 1) == n:
            halfPower = int(n / 2)
            half = self.myPow(x, halfPower)
            return half * half
        else:
            return x * self.myPow(x, n -1)
