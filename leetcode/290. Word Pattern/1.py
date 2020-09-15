# Complexity (n = number of words in the string)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        words = string.split(' ')
        if len(pattern) != len(words):
            return False

        pattern_map = {}
        mapped_words = set()
        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]
            if letter not in pattern_map:
                if word not in mapped_words:
                    pattern_map[letter] = word
                    mapped_words.add(word)
                else:
                    return False
            else:
                if pattern_map[letter] != word:
                    return False

        return True
