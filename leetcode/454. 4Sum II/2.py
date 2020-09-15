# Complexity(n = max input list length)
# Time complexity: O(n^2)
# Space complexity: O(n^2)
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = {}
        for a in A:
            for b in B:
                if a + b not in AB:
                    AB[a + b] = 1
                else:
                    AB[a + b] += 1

        sums = 0
        for c in C:
            for d in D:
                if - (c + d) in AB:
                    sums += AB[- (c + d)]

        return sums
