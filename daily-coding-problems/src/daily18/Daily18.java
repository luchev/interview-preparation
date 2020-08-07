package daily18;

import java.util.ArrayDeque;
import java.util.ArrayList;

class Daily18 {
    private ArrayDeque<Integer> window = new ArrayDeque<>();

    /**
     * Compute the maximum value of each subarray of length K = windowSize
     *
     * Complexity (n = input size, k = window size)
     * Time complexity: O(n)
     * Space complexity: O(k)
     *
     * @param input - int array
     * @param windowSize - size of the moving window
     * @return - int array where each item is the max item in the moving window (subarray)
     */
    ArrayList<Integer> solve(int[] input, int windowSize) {
        window.clear();
        // Keep track of the largest indices
        ArrayList<Integer> output = new ArrayList<>();

        for (int i = 0; i < input.length; i++) {
            // If an index is out of the window boundary - remove it
            while (!window.isEmpty() && window.getFirst() <= i - windowSize) {
                window.removeFirst();
            }

            // Remove from the back all items smaller than the current item as they are not needed
            // There is no use keeping smaller integers to the left in the array, they cannot be
            // the max in the subarray
            while (!window.isEmpty() && input[window.getLast()] <= input[i]) {
                window.removeLast();
            }

            // Add the current index, if it is unneeded it will be removed by the above loops next round
            window.add(i);

            // If we have a full window (omit the first k - 1 items - they don't make a full window)
            // we have an answer sitting at the front of the dequeue
            if (i >= windowSize - 1) {
                output.add(input[window.getFirst()]);
            }
        }

        return output;
    }
}
