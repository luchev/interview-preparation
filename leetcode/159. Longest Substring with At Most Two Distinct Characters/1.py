# Complexity (n = length of word)
# Time complexity: O(n)
# Space complexity: O(1) because the dictionary is always of fixed size <= 2

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        slow = 0

        max_len = 0
        window = defaultdict(int)
        for fast, char in enumerate(s):
            window[char] += 1
            while len(window) > 2:
                window[s[slow]] -= 1
                if window[s[slow]] <= 0:
                    del window[s[slow]]
                slow += 1
            max_len = max(max_len, fast - slow + 1)

        return max_len
