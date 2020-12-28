# Complexity (n = target)
# Time complexity: O(sqrt(n))
# Space complexity: O(1)

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        if target % 2 == 0:
            return k
        elif k % 2 == 0:
            return k + 1
        else:
            return k + 2
