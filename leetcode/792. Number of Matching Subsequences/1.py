# Complexity (n = number of words, k = max word length, z = length of x)
# Time complexity: O(s + k * n)
# Space complexity: O(n)

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        que = defaultdict(list)
        for x in words:
            que[x[0]].append(x[1:])
        
        for char in s:
            oldList = que[char]
            que[char] = []
            for suffix in oldList:
                if len(suffix) == 0:
                    result += 1
                else:
                    que[suffix[0]].append(suffix[1:])
        
        return result
