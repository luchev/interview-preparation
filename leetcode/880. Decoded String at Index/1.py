# Complexity (n = length of S)
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        length = 0
        for char in S:
            if char.isdigit():
                length *= int(char)
            else:
                length += 1

        for char in reversed(S):
            K %= length
            if K == 0 and char.isalpha():
                return char

            if char.isdigit():
                length /= int(char)
            else:
                length -= 1

        return None
