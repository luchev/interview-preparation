class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z = ord('z') - ord('a')
        out = []
        for i in range(n):
            char = min(z, k - n)
            k -= char
            out.append(chr(char + ord('a')))
        return ''.join(reversed(out))
