# Complexity (n = input number)
# Time complexity: O( log(n) ) log(n) is the number of bits the number has
# Space complexity: O(1)

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return ~N & (2 ** (len(bin(N)) - 2) - 1)
        # We need a mask to remove the right bits from negation (which is the same as compliment)
        # To construct the mask:
        # Most significant bit + 1 = len(bin(N)) - 2
        # Get a number with the bit after the most significant set = 2 ** (most significant bit + 1) = 100...00
        # Mask = Subtract 1 from 100...00 to get 11...11

        # Negate the original number
        # AND the negated original number and the mask to get only the right bits of the compliment
