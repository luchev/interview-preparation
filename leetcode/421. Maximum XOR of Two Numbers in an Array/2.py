# Complexity (n = input array size)
# Time complexity: O(n) with a large constant
# Space complexity: O(1)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_bits = len(bin(max(nums))[2:])
        max_num = 0
        for i in reversed(range(max_bits)):
            max_num <<= 1
            potential_new_max = max_num | 1
            prefixes = set(num >> i for num in nums)
            if any(potential_new_max ^ prefix in prefixes for prefix in prefixes):
                max_num = potential_new_max
        return max_num
