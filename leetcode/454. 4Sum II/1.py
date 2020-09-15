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

        CD = {}
        for c in C:
            for d in D:
                if c + d not in CD:
                    CD[c + d] = 1
                else:
                    CD[c + d] += 1

        sums = 0
        for ab in AB:
            if -ab in CD:
                sums += AB[ab] * CD[-ab]

        return sums
