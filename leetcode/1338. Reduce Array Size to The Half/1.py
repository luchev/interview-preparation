# Complexity (n = length of input array)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = sorted(collections.Counter(arr).values())
        half = len(arr) / 2
        result = 0
        while half > 0:
            half -= counts.pop()
            result += 1
        return result