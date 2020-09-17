# Complexity (n = number of items in the list, k = largest number)
# Time complexity: O(n)
# Space complexity: O(2 ^ log(k)) to construct the trie

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_bits = len(bin(max(nums))[2:])
        max_xor = 0
        trie = {}

        # add each number to the bit trie
        for num in nums:
            binary = bin(num)[2:]
            binary = '0' * (max_bits - len(binary)) + binary

            # keep track of the max xor for the current number
            current_xor = 0
            # node in the trie to xor with the current number
            xor_node = trie

            # pointer in the trie for the current number
            num_node = trie
            for bit in binary:
                # add each bit to the trie
                if bit not in num_node:
                    num_node[bit] = {}
                num_node = num_node[bit]

                # calculate the max xor for num
                opposite_bit = '0' if bit == '1' else '1'
                if opposite_bit in xor_node:
                    current_xor = (current_xor << 1) | 1
                    xor_node = xor_node[opposite_bit]
                else:
                    current_xor = (current_xor << 1)
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, current_xor)

        return max_xor
