# Complexity (n = max(length of A, length of B))
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        mismatched_indices = []
        for i in range(len(A)):
            if A[i] != B[i]:
                mismatched_indices.append(i)

        if len(mismatched_indices) > 2 or len(mismatched_indices) == 1:
            return False
        elif len(mismatched_indices) == 2:
            index_one, index_two = mismatched_indices
            if A[index_one] == B[index_two] and A[index_two] == B[index_one]:
                return True
        elif len(mismatched_indices) == 0:
            characters = set()
            for char in A:
                if char not in characters:
                    characters.add(char)
                else:
                    return True
        return False
