# Complexity (n = input list size)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        minEl = min(nums)
        maxEl = max(nums)
        bucketSize = max(1, (maxEl - minEl) // (len(nums) - 1))
        nBuckets = (maxEl - minEl) // bucketSize + 1
        buckets = [[+math.inf, -math.inf, False] for _ in range(nBuckets)]
        
        for x in nums:
            bucketIdx = math.floor((x - minEl) / bucketSize)
            buckets[bucketIdx][0] = min(buckets[bucketIdx][0], x)
            buckets[bucketIdx][1] = max(buckets[bucketIdx][1], x)
            buckets[bucketIdx][2] = True
        
        lastBucketMax = minEl
        result = 0
        for bucket in buckets:
            if not bucket[2]:
                continue
            result = max(result, bucket[0] - lastBucketMax)
            lastBucketMax = bucket[1]
        return result