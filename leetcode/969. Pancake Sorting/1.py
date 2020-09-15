# Complexity (n = number of items in the list)
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ks = []
        for i in range(len(A) - 1, 0, -1):
            maxIndex = self.findMaxIndex(A[:i + 1])
            if maxIndex != i:
                ks.append(maxIndex + 1)
                self.reverseUntilIndex(A, maxIndex + 1)
                ks.append(i + 1)
                self.reverseUntilIndex(A, i + 1)

        return ks

    def findMaxIndex(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return -1
        maxIndex = 0
        for i in range(len(arr)):
            if arr[i] > arr[maxIndex]:
                maxIndex = i
        return maxIndex

    def reverseUntilIndex(self, arr: List[int], index) -> None:
        arr[:index] = arr[:index][::-1]
