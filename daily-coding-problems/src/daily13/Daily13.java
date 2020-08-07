package daily13;

import java.util.HashMap;

class Daily13 {
    /**
     * Calculate the length of the longest substring composed with at most K distinct characters
     *
     * For loop to move the end position of the currently processed substring
     * While loop to move the start position of the currently processed substring
     *
     * It might seem we should have O(N^2) complexity because of the nested loops but
     * the for-loop does exactly N iterations. The while loop moves the starting index which is always less than
     * the end index and it grows monotonously so the while loop really does N iterations throughout the whole
     * execution of the program.
     *
     * Complexity (n = length of input string)
     * Time complexity: O(n)
     * Space complexity: O(n), it's really O(k) but worst case it becomes O(n)
     *
     * @param input - string to find longest subsring with K chars
     * @param differentCharacters - number of distinct characters allowed in a substring (aka K)
     * @return - length of longest substring composed of <= K different characters
     */
    static int solve(String input, int differentCharacters) {
        // Check if K is legit or we can just return the answer without any calculations
        if (differentCharacters < 1) {
            return 0;
        }

        // Keep the <character:count> for the characters in input[currentStart, currentEnd]
        // indices are inclusive
        HashMap<Character, Integer> charSeenTimes = new HashMap<>();
        // Keep track of the best substring so far, we only need the length but this can be easily modified to
        // return the substring itself
        int bestStart = 0;
        int bestEnd = 0;
        // Keep a front index iterator, we work on a moving window with varying size determined by
        // [currentStart, currentEnd]
        int currentStart = 0;

        // Move the currentEnd position
        for (int currentEnd = 0; currentEnd < input.length(); currentEnd++) {
            // Check if we need to process the current character
            // Either add it to the hash or increment its value
            char currentChar = input.charAt(currentEnd);
            if (charSeenTimes.containsKey(currentChar)) {
                charSeenTimes.put(currentChar, charSeenTimes.get(currentChar) + 1);
            } else {
                charSeenTimes.put(currentChar, 1);
            }

            // Move the currentStart position until we have a substring containing no more than K distinct characters
            while (currentStart < currentEnd && charSeenTimes.size() > differentCharacters) {
                char frontChar = input.charAt(currentStart);
                charSeenTimes.put(frontChar, charSeenTimes.get(frontChar) - 1);
                if (charSeenTimes.get(frontChar) == 0) {
                    charSeenTimes.remove(frontChar);
                }
                currentStart++;
            }

            // Check if the current substring is better than the previous best
            if (currentEnd - currentStart > bestEnd - bestStart) {
                bestStart = currentStart;
                bestEnd = currentEnd;
            }
        }

        // Because our indices are inclusive we need +1
        return bestEnd - bestStart + 1;
    }
}
