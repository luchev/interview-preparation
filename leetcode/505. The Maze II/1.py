# Complexity (n = maze rows, k = maze columns)
# Time complexity: O(n * k * log(n * k))
# Space complexity: O(n * k)

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = set()
        heap = [(0, start[0], start[1])] # squares, row, col
        
        while heap:
            squares, curRow, curCol = heapq.heappop(heap)
            if (curRow, curCol) in visited:
                continue
            visited.add((curRow, curCol))
            if destination == [curRow, curCol]:
                return squares
            
            # go up,down,right,left
            for drow, dcol in [(0, +1), (0, -1), (+1, 0), (-1, 0)]:
                nextRow = curRow
                nextCol = curCol
                dist = 0
                while 0 <= nextRow + drow < len(maze) and 0 <= nextCol + dcol < len(maze[0]) and maze[nextRow + drow][nextCol + dcol] != 1:
                    nextRow += drow
                    nextCol += dcol
                    dist += 1
                heapq.heappush(heap, (squares + dist, nextRow, nextCol))
            
        return -1