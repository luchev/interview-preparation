# Complexity (n = length of the string)
# Time complexity: O(n^2)
# Space complexity: O(n)

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        que = [0]
        visited = set()
        while len(que) > 0:
            start = que.pop()
            if start in visited:
                continue
            visited.add(start)

            if start >= len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in words:
                    que.append(end)

        return False
