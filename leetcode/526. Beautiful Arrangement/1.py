# Complexity (n = size of array, k = number of beautiful arrangements)
# Time complexity: O(k)
# Space complexity: O(n)

class Solution:
    def countArrangement(self, n: int) -> int:
        return self.backtrack(n, 1, [False] * (n + 1))
    
    def backtrack(self, n, current, visited):
        if current > n:
            return 1
        count = 0
        for i in range(1, n + 1):
            if not visited[i] and (current % i == 0 or i % current == 0):
                visited[i] = True
                count += self.backtrack(n, current + 1, visited)
                visited[i] = False
        return count
