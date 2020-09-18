# Complexity (n = length of string, k = sequence length)
# Time complexity: O( (n-k) * k )
# Space complexity: O( (n-k) * k )

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_len = 10
        sequences = set()
        repeated_sequences = set()

        for start in range(len(s) - sequence_len + 1):
            window = s[start:start + sequence_len]

            if window in sequences:
                repeated_sequences.add(window)
            sequences.add(window)

        return repeated_sequences
