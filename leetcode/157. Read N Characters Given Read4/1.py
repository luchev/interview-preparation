# Complexity (n = characters to read)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        read_chars = 0
        write_index = 0
        while read_chars < n:
            buf4 = [' '] * 4
            read_chars4 = read4(buf4)
            if read_chars4 == 0:
                break
            read_chars += read_chars4
            for i in range(read_chars4):
                buf[write_index] = buf4[i]
                write_index += 1
        return min(n, read_chars)


"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


def read4(buffer):
    pass
