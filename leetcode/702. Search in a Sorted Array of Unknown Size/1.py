# Complexity (n = array's length)
# Time complexity: O(log(n))
# Space complexity: O(1)


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:
#       pass

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = self.find_interval(reader, target)
        return self.bst(reader, target, left, right)

    def find_interval(self, reader, target):
        step = 1
        left = 0
        right = step
        while reader.get(right) < target:
            step *= 2
            left, right = right, step
        return left, right

    def bst(self, reader, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            mid_val = reader.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
