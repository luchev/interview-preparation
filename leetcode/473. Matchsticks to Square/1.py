# Complexity (n = number of matchsticks)
# Time complexity: O(n^4)
# Space complexity: O(n)

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        quarter = sum(matchsticks) // 4
        if quarter * 4 != sum(matchsticks):
            return False
        
        matchsticks.sort(reverse=True)
        sides = [0,0,0,0]
        def dfs(current: int):
            if current == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            for i in range(4):
                sides[i] += matchsticks[current]
                if sides[i] <= quarter and dfs(current + 1):
                    return True
                sides[i] -= matchsticks[current]
            return False
                
        return dfs(0)