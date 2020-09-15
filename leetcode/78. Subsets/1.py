# Complexity (n = number of items in the list)
# Time complexity: O(n * 2^n)
# Space complexity: O(n * 2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        indices = [False for x in range(len(nums))]
        subsets = []
        
        for i in range(2 ** len(nums)):
            subset = []
            for k in range(len(indices)):
                if indices[k]:
                    subset.append(nums[k])
            subsets.append(subset)
            self.plus_one(indices)
        
        return subsets
    
    def plus_one(self, arr: List[bool]) -> None:
        for i in reversed(range(len(arr))):
            arr[i] = not arr[i]
            if arr[i]:
                break
