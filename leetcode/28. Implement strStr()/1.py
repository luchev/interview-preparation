# Complexity (n = haystack length, k = needle length)
# Time complexity: O(n * k)
# Space complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0

        for haystackIndex in range(len(haystack) - len(needle) + 1):
            match = True
            for needleIndex in range(len(needle)):
                if haystack[haystackIndex + needleIndex] != needle[needleIndex]:
                    match = False
                    break
            if match:
                return haystackIndex

        return -1
