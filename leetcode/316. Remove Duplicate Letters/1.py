# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1) because we have a limited aphabet

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: index for index, char in enumerate(s)}
        seq = []
        sequence_chars = set()
        for index, char in enumerate(s):
            if char not in sequence_chars:
                seq.append(char)
                sequence_chars.add(char)
            while len(seq) >= 2 and ord(seq[-2]) > ord(seq[-1]) and last_occurrence[seq[-2]] > index:
                print(seq, index, char)
                seq.pop()
                sequence_chars.remove(seq.pop())
                seq.append(char)
        return ''.join(seq)
