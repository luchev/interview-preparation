# Complexity (n = rows in the matrix, m = columns in the matrix)
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from typing import List
from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        next_board = deepcopy(board)
        for row in range(len(board)):
            for col in range(len(board[row])):
                neighbours = countNeighbours(board, row, col)
                if board[row][col] == 1 and neighbours < 2:
                    next_board[row][col] = 0
                elif board[row][col] == 1 and 3 < neighbours:
                    next_board[row][col] = 0
                elif board[row][col] == 0 and neighbours == 3:
                    next_board[row][col] = 1

        for row in range(len(board)):
            for col in range(len(board[row])):
                board[row][col] = next_board[row][col]


shifts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def countNeighbours(board: List[List[int]], row: int, col: int) -> int:
    ones = 0
    for drow, dcol in shifts:
        current_row = row + drow
        current_col = col + dcol
        if 0 <= current_row < len(board) and 0 <= current_col < len(board[current_row]) and board[current_row][current_col] == 1:
            ones += 1
    return ones
