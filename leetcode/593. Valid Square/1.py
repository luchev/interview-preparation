# Complexity (n = 4 points of a square)
# Time complexity: O(1)
# Space complexity: O(1)

from typing import List, Tuple


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        p4_dist = [dist(p4, p) for p in points if p != p4]
        if len(p4_dist) != 3:
            return False
        diag = max(p4_dist)
        diag_point = p4_dist.index(diag)

        side = min(p4_dist)
        side_points = [i for i, d in enumerate(p4_dist) if d == side]
        if len(side_points) != 2:
            return False

        for point in side_points:
            if dist(points[diag_point], points[point]) != side:
                return False

        if dist(points[side_points[0]], points[side_points[1]]) != diag:
            return False

        return True


def dist(A: Tuple[int, int], B: Tuple[int, int]):
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** .5
