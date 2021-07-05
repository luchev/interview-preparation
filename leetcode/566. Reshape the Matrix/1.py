# Complexity (n = matrix rows, m = matrix columns)
# Time complexity: O(n * m)
# Space complexity: O(n * m) for the answer, otherwise O(1)

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        newMatrix = [[0] * c for _ in range(r)]
        iRow = 0
        iCol = 0
        for row in mat:
            for x in row:
                newMatrix[iRow][iCol] = x
                iCol += 1
                if iCol == c:
                    iRow += 1
                    iCol = 0
        return newMatrix