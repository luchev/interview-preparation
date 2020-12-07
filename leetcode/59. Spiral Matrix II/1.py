# Complexity (n = spiral matrix dimension)
# Time complexity: O(n^2)
# Space complexity: O(1) excluding the output matrix

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [ [0] * n for _ in range(n) ]
        directions = {
            'R': [(+1,0), 'D'],
            'D': [(0,+1), 'L'],
            'L': [(-1,0), 'U'],
            'U': [(0,-1), 'R'],
        }
        
        x = 0
        y = 0
        current_direction = 'R'
        for i in range(1, n ** 2 + 1):
            matrix[y][x] = i
            
            x_shift, y_shift = directions[current_direction][0]
            next_x = x + x_shift
            next_y = y + y_shift
            
            if 0 <= next_x < n and 0 <= next_y < n and matrix[next_y][next_x] == 0:
                x = next_x
                y = next_y
            else:
                current_direction = directions[current_direction][1]
                x_shift, y_shift = directions[current_direction][0]
                x = x + x_shift
                y = y + y_shift

        return matrix
