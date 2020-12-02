# Complexity (n = number turns to determine if Alice can win)
# Time complexity: O(n * sqrt(n))
# Space complexity: O(n)

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        win = [False] * (n + 1)
        for i in range(1, n+1):
                for k in range(1, int(i ** .5) + 1):
                    if win[i - k * k] == False:
                        win[i] = True
                        break
        return win[n]
