# Complexity (n = input list size)
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        sums = [0]
        for x in stones:
            sums.append(sums[-1] + x)
        
        def subSum(left, right):
            return sums[right + 1] - sums[left]
        
        @lru_cache(2000)
        def minmax(left, right, isAlice):
            if left == right:
                return 0
            if isAlice:
                return max(
                    minmax(left + 1, right, not isAlice) + subSum(left+1, right),
                    minmax(left, right - 1, not isAlice) + subSum(left, right - 1)    
                )
            else:
                return min(
                    minmax(left + 1, right, not isAlice) - subSum(left+1, right),
                    minmax(left, right - 1, not isAlice) - subSum(left, right - 1)
                )
                
        return minmax(0, len(stones) - 1, True)