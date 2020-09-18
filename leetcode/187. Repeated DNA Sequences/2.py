# Complexity (n = length of string, k = sequence length)
# Time complexity: O( n )
# Space complexity: O( n - k )

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_len = 10

        if len(s) <= sequence_len:
            return []

        # Rabin-Karp rolling hash
        mapped = self.mapAlphabet(s)
        alphabet_size = len(mapped)
        remove_multiplier = pow(alphabet_size, sequence_len)

        sequences = set()
        repeated_sequences = set()
        hash_value = 0
        for start in range(len(s)):
            hash_value = hash_value * alphabet_size + mapped[s[start]]
            if start >= sequence_len:
                hash_value -= mapped[s[start - sequence_len]] * remove_multiplier

            if start >= sequence_len - 1:
                if hash_value in sequences:
                    repeated_sequences.add(
                        s[start - sequence_len + 1:start + 1])
                sequences.add(hash_value)

        return repeated_sequences

    def mapAlphabet(self, s: str) -> {}:
        mapping = {}
        current_index = 0
        for char in s:
            if char not in mapping:
                mapping[char] = current_index
                current_index += 1
        return mapping
