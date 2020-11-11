# Complexity (n = 4 points of a square)
# Time complexity: O(1)
# Space complexity: O(1)

from typing import List, Tuple

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        dists = set()
        for i in range(len(points)):
            for k in range(i + 1, len(points)):
                dist_curr = dist(points[i], points[k])
                if dist_curr == 0:
                    return False
                dists.add(dist_curr)
        return len(dists) == 2
        
        
def dist(A: Tuple[int, int], B:Tuple[int, int]):
    return ( (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 ) ** .5
