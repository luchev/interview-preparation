# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

import functools
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        split_zeros = self.split_list(nums, 0)
        max_product = max([self.max_product_without_zero(subarr)
                           for subarr in split_zeros])
        if len(split_zeros) > 1 or nums[0] == 0 or nums[-1] == 0:
            return max(max_product, 0)
        return max_product

    def max_product_without_zero(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        negative_numbers = self.count_negatives(nums)
        if negative_numbers % 2 == 0:
            return math.prod(nums)
        else:
            first_negative_index, last_negative_index = self.first_and_last_negative_index(
                nums)
            return max(math.prod(nums[first_negative_index + 1:]), math.prod(nums[0:last_negative_index]))

    def count_negatives(self, nums: List[int]) -> int:
        return functools.reduce(lambda negatives, x: negatives + 1 if x < 0 else negatives, nums, 0)

    def first_and_last_negative_index(self, nums: List[int]) -> (int, int):
        first_index = -1
        for i in range(len(nums)):
            if nums[i] < 0:
                first_index = i
                break
        last_index = -1
        for i in reversed(range(len(nums))):
            if nums[i] < 0:
                last_index = i
                break
        return (first_index, last_index)

    def split_list(self, arr, splitter):
        splits = [[]]
        for i in arr:
            if i != splitter:
                splits[-1].append(i)
            else:
                if len(splits[-1]) != 0:
                    splits.append([])
        if len(splits[-1]) == 0 and len(arr) != 0:
            splits.pop()
        return splits
