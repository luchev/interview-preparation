# Complexity (n = board size)
# Time complexity: O(n!)
# Space complexity: O(n)

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, diags, adiags, cols, state):
            if row == n:
                result.append(makeBoard(state))
            
            for col in range(n):
                diag = row - col
                adiag = row + col
                if col in cols or diag in diags or adiag in adiags:
                    continue
                
                cols.add(col)
                diags.add(diag)
                adiags.add(adiag)
                state[row][col] = 'Q'
                
                backtrack(row + 1, diags, adiags, cols, state)
                
                cols.remove(col)
                diags.remove(diag)
                adiags.remove(adiag)
                state[row][col] = '.'
        
        result = []
        board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result
    
def makeBoard(state):
    return ["".join(row) for row in state]