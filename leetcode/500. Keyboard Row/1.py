# Complexity (n = sum of the lengths of all words)
# Time complexity: O(n)
# Space complexity: O(1) the sets are using memory but it's constant because the alphabet is limited (26)

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboardRows = [
            set([char for char in 'qwertyuiop']),
            set([char for char in 'asdfghjkl']),
            set([char for char in 'zxcvbnm']),
        ]
        
        result = []
        for word in words:
            for row in keyboardRows:
                isOneRowWord = True
                for char in word.lower():
                    if char not in row:
                        isOneRowWord = False
                if isOneRowWord:
                    result.append(word)
                    break

        return result
