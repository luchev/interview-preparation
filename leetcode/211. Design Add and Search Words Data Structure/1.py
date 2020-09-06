# Complexity(n = input word length, k = alphabet size)
# Add word Time complexity: O(n)
# Find word Time complexity without wildcards: O(n)
# Find word Time complexity with wildcards: O(k^n)
# Space complexity: O(n * k) but much better in reality

class TrieNode:
    def __init__(self):
        self.isWordEnd = False
        self.transitions = {}

    def addTransition(self, letter: str):
        self.transitions[letter] = TrieNode()

    def getTransition(self, letter: str):
        try:
            return self.transitions[letter]
        except:
            return None

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        pointer = self.root
        for char in word:
            if pointer.getTransition(char) is None:
                pointer.addTransition(char)
            pointer = pointer.getTransition(char)

        pointer.isWordEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search_recursive(self.root, word)

    def _search_recursive(self, root: TrieNode, word: str) -> bool:
        """
        Returns if the word can be found following the transitions in the trie
        """
        if root is None:
            return False

        if len(word) == 0:
            if root.isWordEnd:
                return True
            else:
                return False

        if word[0] != '.':
            return self._search_recursive(root.getTransition(word[0]), word[1:])
        else: # word[0] == '.'
            for transition in root.transitions:
                if self._search_recursive(root.transitions[transition], word[1:]):
                    return True

            return False
