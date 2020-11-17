# Complexity (p = square side, q = first intersection of the ray with the left square side)
# Time complexity: O(log(p))
# Space complexity: O(1)

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd_pq = gcd(p, q)
        if (p / gcd_pq) % 2 == 1 and (q / gcd_pq) % 2:
            return 1
        elif (p / gcd_pq) % 2 == 1:
            return 0
        else:
            return 2


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
