# Complexity (n = number of items in the list)
# Time complexity: O(n) amortized
# Space complexity: O(1)

# Idea for the algorithm:
# If we find the median to be M and split the array in [x <= M] and [x >= M]
# Then we can find the major2, which appears > n/2 times, in both of these subarrays
# major2 is a potential major, which appears > n/3 times, for the whole array
# The median is also a potential major, which appears > n/3 times, for the whole array
# In the end we count the occurrences of the median and the 2 potential majors from the left and right
# subarray and if any of them are seen > n/3 times, we append them to the resulting array

from random import randint
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        median = quickSelect(nums, len(nums)//2)

        potential_major_left = majorityElementHalf(nums, 0, len(nums)//2)
        potential_major_right = majorityElementHalf(
            nums, len(nums)//2 + 1, len(nums))

        majors = set()
        potential_majors = [
            median, potential_major_left, potential_major_right]
        for potential in potential_majors:
            if nums.count(potential) > len(nums) / 3:
                majors.add(potential)

        return list(majors)


def majorityElementHalf(nums: List[int], left: int, right: int) -> int:
    count = 0
    candidate = 0
    for i in range(left, right):
        x = nums[i]
        if count == 0:
            candidate = x

        if x == candidate:
            count += 1
        else:
            count -= 1
    return candidate


def quickSelect(nums: List[int], index: int, left: int = 0, right: int = None):
    if right is None:
        right = len(nums) - 1
    if left == right:
        return nums[left]

    splitter_index = randint(left, right)
    pos = partition(nums, splitter_index, left, right)
    if pos == index:
        return nums[pos]
    elif pos < index:
        return quickSelect(nums, index, pos + 1, right)
    else:
        return quickSelect(nums, index, left, pos - 1)


def partition(nums: List[int], splitter: int, left: int, right: int):
    splitter_val = nums[splitter]
    nums[splitter], nums[right] = nums[right], nums[splitter]
    splitter = left
    for left in range(left, right):
        if nums[left] < splitter_val:
            nums[left], nums[splitter] = nums[splitter], nums[left]
            splitter += 1
    nums[splitter], nums[right] = nums[right], nums[splitter]
    return splitter
