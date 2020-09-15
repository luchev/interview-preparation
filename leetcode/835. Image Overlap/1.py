# Complexity (n = matrix dimension)
# Time complexity: O(n^4)
# Space complexity: O(1)

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        return max(self.calcMaxOverlap(A, B), self.calcMaxOverlap(B, A))

    def calcMaxOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        maxOnes = 0
        for startRow in range(len(A)):
            for startCol in range(len(A[startRow])):
                ones = 0
                for row in range(len(B) - startRow):
                    for col in range(len(B[row]) - startCol):
                        if A[startRow + row][startCol + col] == B[row][col]:
                            if B[row][col] == 1:
                                ones += 1
                maxOnes = max(maxOnes, ones)
        return maxOnes
