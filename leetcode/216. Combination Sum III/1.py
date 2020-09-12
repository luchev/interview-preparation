# Complexity (n = target number, k = set size)
# Time complexity: O(9! / (9 - k)!) but much better in reality because we can stop early
# Space complexity: O(k) without the space required for the answer
# https://leetcode.com/problems/combination-sum-iii/solution/685974 for time complexity analysis

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 and n == 0:
            return [[]]

        if n > sum([x for x in range(1, 10)]):
            return []

        self.combinations = []
        for i in range(1, 10):
            self.sumUnique(k, n, [i], i)
        return self.combinations

    def sumUnique(self, number_count: int, targetSum: int, currentSet: List[int], currentSum: int) -> None:
        if number_count == len(currentSet) and currentSum == targetSum:
            self.combinations.append(currentSet.copy())
            return
        elif number_count < len(currentSet) or targetSum < currentSum:
            return

        for i in range(currentSet[-1] + 1, 10):
            currentSet.append(i)
            self.sumUnique(number_count, targetSum, currentSet, currentSum + i)
            currentSet.pop()
