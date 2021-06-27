# Complexity (n = input list size)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        fromLeft = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                fromLeft[i] = fromLeft[i - 1] + 1
                
        fromRight = [1] * len(ratings)
        for i in reversed(range(0, len(ratings) - 1)):
            if ratings[i] > ratings[i + 1]:
                fromRight[i] = fromRight[i + 1] + 1
        
        return sum(max(x,y) for x,y in zip(fromLeft, fromRight))