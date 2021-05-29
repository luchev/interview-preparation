# Complexity (n = board size)
# Time complexity: O(n!)
# Space complexity: O(n)
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diags, adiags, cols):
            if row == n:
                nonlocal result
                result += 1

            for col in range(n):
                diag = row - col
                adiag = row + col
                if col in cols or diag in diags or adiag in adiags:
                    continue
                
                cols.add(col)
                diags.add(diag)
                adiags.add(adiag)
                
                backtrack(row + 1, diags, adiags, cols)
                
                cols.remove(col)
                diags.remove(diag)
                adiags.remove(adiag)
        
        result = 0
        backtrack(0, set(), set(), set())
        return result