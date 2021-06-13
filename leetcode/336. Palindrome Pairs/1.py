# Complexity (n = number of words, k = max word length)
# Time complexity: O(n * k^2)
# Space complexity: O((n + k)^2)

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wordMap = {word: i for i,word in enumerate(words)}
        result = []
        
        for index, word in enumerate(words):
            if word[::-1] in wordMap and index != wordMap[word[::-1]]:
                result.append((index, wordMap[word[::-1]]))
            
            for suffix in suffixes(word):
                if suffix[::-1] in wordMap and wordMap[suffix[::-1]] != index:
                    result.append((wordMap[suffix[::-1]], index))
            
            for prefix in prefixes(word):
                if prefix[::-1] in wordMap and wordMap[prefix[::-1]] != index:
                    result.append((index, wordMap[prefix[::-1]]))
        return result
        
def prefixes(word):
    result = []
    for i in range(len(word)):
        if word[i:] == word[i:][::-1]:
            result.append(word[:i])
    return result

def suffixes(word):
    result = []
    for i in range(len(word)):
        if word[:i+1] == word[:i+1][::-1]:
            result.append(word[i+1:])
    return result