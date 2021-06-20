# Complexity (n = matrix rows = matrix columns)
# Time complexity: O(n^2 * log(n))
# Space complexity: O(n^2)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        que = [(grid[0][0],0,0)]
        while que:
            priority,x,y = heapq.heappop(que)
            if visited[x][y]:
                continue
            visited[x][y] = True
            if (x,y) == (n-1,n-1):
                return priority
            
            for dx,dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                nextX = x + dx
                nextY = y + dy
                if 0 <= nextX < n and 0 <= nextY < n:
                    heapq.heappush(que, (max(priority, grid[nextX][nextY]), nextX, nextY))
        
        return math.inf