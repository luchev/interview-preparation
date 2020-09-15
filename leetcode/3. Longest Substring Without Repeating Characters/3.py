# Complexity (n = input length)
# Time complexity: O(n)
# Space complexity: O(ALPHABET_SIZE)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_len = 0
        slow_index = 0
        for fast_index, char in enumerate(s):
            while char in window:
                window.remove(s[slow_index])
                slow_index += 1
            window.add(char)

            max_len = max(max_len, len(window))

        return max_len
