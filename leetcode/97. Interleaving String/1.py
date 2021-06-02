# Complexity (n = length of s1, k = length of s2)
# Time complexity: O(n * k)
# Space complexity: O(n * k)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        @cache
        def check(s1_i, s2_i, s3_i):
            if s3_i == len(s3):
                return True
            if s1_i < len(s1) and s1[s1_i] == s3[s3_i] and check(s1_i + 1, s2_i, s3_i + 1):
                return True
            if s2_i < len(s2) and s2[s2_i] == s3[s3_i] and check(s1_i, s2_i + 1, s3_i + 1):
                return True
            return False
        
        return check(0, 0, 0)