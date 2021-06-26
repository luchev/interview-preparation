# Complexity (n = input list size, k = difference between largest and smallest number)
# Time complexity: O(n * log(k))
# Space complexity: O(k)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(index, value, tree, size):
            index += size
            tree[index] += value
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]
        
        def query(left, right, tree, size):
            result = 0
            left += size
            right += size
            while left < right:
                if left % 2 == 1:
                    result += tree[left]
                    left += 1
                left //=2
                
                if right % 2 == 1:
                    right -= 1
                    result += tree[right]
                right //= 2
            return result
        
        offset = 10 ** 4
        size = 2 * offset + 1
        tree = [0] * (2 * size)
        result = []
        for num in reversed(nums):
            result.append(query(0, num + offset, tree, size))
            update(num + offset, 1, tree, size)
        return reversed(result)