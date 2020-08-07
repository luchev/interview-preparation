package daily4;

class Daily4 {
    /**
     * Complexity (n = array size):
     * Time complexity: O(n)
     * Space complexity: O(1)
     *
     * Attention: the array is modified to achieve O(1) space complexity
     *
     * @param array - array of ints to find the smallest positive int that is not within
     * @return - return the smallest positive int that is not within the array
     */
    static int solve(int[] array) {
        // Traverse the array and if you find a number such that the number is less than the current INDEX
        // swap the number to be on position INDEX in the array
        // Basically put each number on index (number - 1)
        for (int i = 0; i < array.length; i++) {
            if (0 < array[i] && array[i] <= i) {
                int tempRight = array[array[i] - 1];
                array[array[i] - 1] = array[i];
                array[i] = tempRight;
            }
        }

        // Traverse the array and the first number that is not equal to its index -1 return it
        // e.g on position 0 we must have 1, on position 2 we must have 1, etc.
        for (int i = 0; i < array.length; i++) {
            if (array[i] != i + 1) {
                return i + 1;
            }
        }

        // If all the numbers in the array satisfy the above condition the array contains all positive
        // numbers in the range [1, array.length] so return the next positive number which is array.length + 1
        return array.length + 1;
    }
}
