# Complexity (n = length of word, k = number of distinct characters allowed in a substring)
# Time complexity: O(n)
# Space complexity: O(k) for the dictionary

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        slow = 0

        max_len = 0
        window = defaultdict(int)
        for fast, char in enumerate(s):
            window[char] += 1
            while len(window) > k:
                window[s[slow]] -= 1
                if window[s[slow]] <= 0:
                    del window[s[slow]]
                slow += 1
            max_len = max(max_len, fast - slow + 1)

        return max_len
