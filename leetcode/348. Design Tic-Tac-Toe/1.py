# Complexity (n = board rows/cols)
# Time complexity: O(1) per operation
# Space complexity: O(n)

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * (2*n + 1)
        self.cols = [0] * (2*n + 1)
        self.diag = 0
        self.adiag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        x = 1 if player == 1 else -1
        
        self.rows[row] += x
        if abs(self.rows[row]) == self.n:
            return player
        
        self.cols[col] += x
        if abs(self.cols[col]) == self.n:
            return player

        if row - col == 0:
            self.diag += x
        if abs(self.diag) == self.n:
            return player
        
        if row + col == self.n - 1:
            self.adiag += x
        if abs(self.adiag) == self.n:
            return player
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)