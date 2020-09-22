# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        candidate1 = None
        count2 = 0
        candidate2 = None

        for x in nums:
            if candidate1 == x:
                count1 += 1
            elif candidate2 == x:
                count2 += 1
            elif count1 == 0:
                candidate1 = x
                count1 = 1
            elif count2 == 0:
                candidate2 = x
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        majors = []
        if nums.count(candidate1) > len(nums) // 3:
            majors.append(candidate1)
        if nums.count(candidate2) > len(nums) // 3:
            majors.append(candidate2)

        return majors
