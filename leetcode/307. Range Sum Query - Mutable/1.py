# Complexity (n = input list size)
# Time complexity for update: O(n)
# Time complexity for sumRange: O(sqrt(n)) 
# Space complexity: O(n)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bucketSize = int(len(nums) ** .5)
        self.numBuckets = math.ceil(len(nums) / self.bucketSize)
        self.buckets = [0] * self.numBuckets
        for i,x in enumerate(nums):
            self.buckets[i // self.numBuckets] += x

    def update(self, index: int, val: int) -> None:
        bucket = index // self.numBuckets
        self.buckets[bucket] = self.buckets[bucket] - self.nums[index] + val
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        result = 0
        start = left // self.numBuckets
        end = right // self.numBuckets
        if start == end:
            return sum(self.nums[left:right+1])
        result += sum(self.buckets[start+1:end])
        result += sum(self.nums[left:(start+1) * self.numBuckets])
        result += sum(self.nums[end * self.numBuckets:right+1])
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)