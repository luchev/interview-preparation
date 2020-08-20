# Complexity(n = rows, m = columns)
# Time complexity: O(n + m)
# Space complexity: O(1)
# This time complexity applies only if we can compute factorials in linear time, which applies for small numbers only.
# Also the space complexity in reality is a lot more because the big factorials exceed 64 bits
# This algorithm performs about the same as a naive DP solution
# We can improve it further by computing the combinations manually

# The idea behind the solution is that we have N rows and M columns, so we want to choose N - 1 times to go down
# and M - 1 times to go right, hence (N - 1 + M - 1) = (N + M - 2).
# We end up with a sequence D R D D R ... where D is down and R is right movement
# In this sequence we have to choose the places to put either the Rs or the Ds hence we need to choose
# (N - 1) positions from (N + M - 2) or (M - 1) positions from (N + M - 2), which are equal
class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        return math.comb(n + m - 2, n - 1)
