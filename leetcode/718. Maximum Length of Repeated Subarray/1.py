# Complexity (n = length of nums1, m = length of nums2)
# Time complexity: O(n * m)
# Space complexity: O(n * m)

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in reversed(range(len(nums1))):
            for k in reversed(range(len(nums2))):
                if nums1[i] == nums2[k]:
                    dp[i][k] = dp[i + 1][k + 1] + 1
        return max(max(x) for x in dp)