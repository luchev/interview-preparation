# Complexity (n = input length)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dset = {}
        for x in nums:
            if x - 1 in dset:
                dset[x-1] = x
            
            if x + 1 in dset:
                dset[x] = x + 1
            else:
                dset[x] = None
        
        lens = {}
        
        def dfs(x: int):
            if x not in dset:
                lens[x] = 0
                return 0
            
            if x in lens:
                return lens[x]
            
            if x + 1 not in lens:
                dfs(x + 1)
            lens[x] = lens[x + 1] + 1
            return lens[x]
        
        return max(dfs(x) for x in nums)