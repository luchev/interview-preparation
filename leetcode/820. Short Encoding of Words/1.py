# Complexity (n = number of words, k = average word length)
# Time complexity: O(n * k)
# Space complexity: O(n * k)

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        leaves = []
        
        for word in set(words):
            ptr = trie
            for char in word[::-1]:
                ptr = ptr[char]
            leaves.append((ptr, len(word) + 1))
        
        return sum(leaf[1] for leaf in leaves if len(leaf[0]) == 0)
