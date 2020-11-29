# Complexity (n = array length)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        visited[start] = True
        stack = [start]
        while stack:
            current = stack.pop()

            if arr[current] == 0:
                return True
            if 0 <= current - arr[current] and not visited[current - arr[current]]:
                stack.append(current - arr[current])
                visited[current - arr[current]] = True
            if current + arr[current] < len(arr) and not visited[current + arr[current]]:
                stack.append(current + arr[current])
                visited[current + arr[current]] = True

        return False
