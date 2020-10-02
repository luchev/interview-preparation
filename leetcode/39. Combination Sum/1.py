# Complexity (n = number of items in the list, t = target)
# Time complexity: O(n^t)
# Space complexity: O(t)

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = set()
        self.target = target
        self.candidates = candidates
        self.backtrack([], 0, 0)
        return self.result

    def backtrack(self, current_set, current_sum, current_index):
        if current_sum == self.target:
            self.result.add(tuple(current_set[:]))
            return
        elif current_sum > self.target:
            return

        for i in range(current_index, len(self.candidates)):
            current_set.append(self.candidates[i])
            self.backtrack(current_set, current_sum + self.candidates[i], i)
            current_set.pop()
