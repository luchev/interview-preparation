# Complexity (n = length of input string)
# Time complexity: O(n * 2^n)
# Space complexity: O(n)

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(s, start, current_set):
            if start == len(s):
                result.append(current_set)

            for i in range(start, len(s)):
                if s[start:i + 1] == s[start:i + 1][::-1]:
                    dfs(s, i + 1, current_set + [s[start:i + 1]])

        dfs(s, 0, [])
        return result
