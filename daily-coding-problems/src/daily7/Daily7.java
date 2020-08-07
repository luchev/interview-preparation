package daily7;

// a = 1, ..., z = 26

import java.util.HashMap;

class Daily7 {
    private String input;
    private HashMap<Integer, Integer> memoizationTwoChar = new HashMap<>();
    private HashMap<Integer, Integer> memoizationOneChar = new HashMap<>();

    /**
     * From the current index:
     * If there is at least one more character to the end of the string - recurse into it
     * If there is at least 2 more characters and they make for a valid encoded char - recurse into it
     * Use memoization to check if we've already computed the given branch in the recursion
     * memoizationOneChar keeps the routes for when reading one char
     * memoizationTwoCHar keeps the routes for when reading 2 chars
     *
     * @param currentIndex - the index we are reading from the string
     */
    private int countDecodeVariantsRecursive(int currentIndex) {
        // If we are at the end of the string - return
        if (currentIndex == input.length()) {
            return 1;
        }

        // Read 1 char
        int oneChar = 0; // ways to decode the following substring if we read one character
        if (currentIndex + 1 <= input.length()) {
            // Check in hash if this route has already been completed before
            if (memoizationOneChar.containsKey(currentIndex)) {
                oneChar = memoizationOneChar.get(currentIndex);
            } else {
                oneChar = countDecodeVariantsRecursive(currentIndex + 1);
                memoizationOneChar.put(currentIndex, oneChar);
            }
        }

        // Read 2 chars
        int twoChar = 0; // ways to decode the following substring if we read two characters
        if (currentIndex + 2 <= input.length()) {
            // Check if we can read 2 characters
            int nextChar = input.charAt(currentIndex);
            int nextNextChar = input.charAt(currentIndex + 1);
            int charsToNumber = (nextChar - '0') * 10 + (nextNextChar - '0');
            if (nextChar != '0' && charsToNumber >= 1 && charsToNumber <= 26) {
                // Check in hash if this route has already been completed before
                if (memoizationTwoChar.containsKey(currentIndex)) {
                    twoChar = memoizationTwoChar.get(currentIndex);
                } else {
                    twoChar = countDecodeVariantsRecursive(currentIndex + 2);
                    memoizationTwoChar.put(currentIndex, twoChar);
                }
            }
        }

        return oneChar + twoChar;
    }

    /**
     * Clear variables and call the recursive count function
     *
     * Complexity (n = length of input):
     * Time complexity: O(n)
     * Space complexity: O(n) for call stack and for hashmaps
     *
     * @param input - string to count the ways it can be decoded
     * @return - how many different ways the input can be decoded
     */
    int countDecodeVariants(String input) {
        this.input = input;
        memoizationOneChar.clear();
        memoizationTwoChar.clear();
        return countDecodeVariantsRecursive(0);
    }
}
