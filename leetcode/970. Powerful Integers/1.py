# Complexity (n = log_x(bound), k = log_y(bound))
# Time complexity: O(n * k)
# Space complexity: O(n * k)

from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xs = [1]
        if x != 1:
            while xs[-1] < bound:
                xs.append(xs[-1] * x)
        ys = [1]
        if y != 1:
            while ys[-1] < bound:
                ys.append(ys[-1] * y)
        
        result = set()
        for x in xs:
            for y in ys:
                if x + y <= bound:
                    result.add(x + y)
        return result