# Complexity (n = number of items in the list)
# Time complexity: O(n * 2^n)
# Space complexity: O(n * 2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            subsets.extend([subset + [num] for subset in subsets])
        return subsets
