package daily12;

import java.util.HashMap;

class Daily12 {
    /**
     * Simply a fibonacci sequence calculated recursively
     *
     * Complexity (n = number of steps)
     * Time complexity: O(2^n)
     *
     * @param stepCount - number of steps in the staircase
     * @return - how many different ways we can climb the staircase with taking 1 or 2 steps at a time
     */
    static int solveStepsOneAndTwoSlow(int stepCount) {
        if (stepCount <= 1) {
            return 1;
        }
        return solveStepsOneAndTwoSlow(stepCount - 1) + solveStepsOneAndTwoSlow(stepCount - 2);
    }


    /**
     * Fibonacci sequence calculated iteratively
     *
     * Complexity (n = number of steps)
     * Time complexity: O(n)
     *
     * @param stepCount - number of steps in the staircase
     * @return - how many different ways we can climb the staircase with taking 1 or 2 steps at a time
     */
    static int solveStepsOneAndTwoFast(int stepCount) {
        int nMinusTwo = 0;
        int nMinusOne = 1;
        // Because we start from 0 we'll have one extra step at the end
        // so nMinusOne will be the correct answer as n (= sum) is stepCount + 1
        for (int i = 0; i < stepCount; i++) {
            int sum = nMinusTwo + nMinusOne;
            nMinusTwo = nMinusOne;
            nMinusOne = sum;
        }
        return nMinusOne;
    }

    /**
     * Solve the problem for any set of allowed steps to be taken at a time, e.g { 1, 3, 5 }
     * Use memoization to improve running time and keep track of already calculated indices
     *
     * Complexity (n = number of steps)
     * Time complexity: O(n)
     *
     * @param stepCount - number of steps in the staircase
     * @return - how many different ways we can climb the staircase with
     * taking steps from the given list of allowed steps
     */

    /**
     * Dictionary used for memoization for the generic step count solver
     */
    private static HashMap<Integer, Integer> computed = new HashMap<>();

    /**
     * Calculate the number of ways one can walk a number of steps given a list of step sizes
     *
     * Complexity (n = number of steps, k = size of allowed steps list)
     * Time complexity: O(k * n)
     * Space complexity: O(n)
     *
     * @param stepCount - number of steps in the staircase
     * @param allowedSteps - a list of steps we can take, e.g {1, 2, 5}
     * @param currentIndex - the position we are currently at
     * @return - how many different ways we can climb the staircase with
     */
    private static int solveStepsRecursive(int stepCount, int[] allowedSteps, int currentIndex) {
        // Out of bounds (invalid step)
        if (currentIndex > stepCount) {
            return 0;
        }

        // We reached the final step
        if (currentIndex == stepCount) {
            return 1;
        }

        // If we have already computed the value for this position return it
        if (computed.containsKey(currentIndex)) {
            return computed.get(currentIndex);
        }

        // Compute the value for the current position by adding up the values with all steps
        int sum = 0;
        for (int step : allowedSteps) {
            int nextIndex = currentIndex + step;
            sum += solveStepsRecursive(stepCount, allowedSteps, nextIndex);
        }

        // Add the new computed value to the computed dictionary
        computed.put(currentIndex, sum);
        return sum;
    }

    /**
     * Calculate the number of ways one can walk a number of steps given a list of step sizes
     *
     * @param stepCount - number of steps in the staircase
     * @param allowedSteps - a list of steps we can take, e.g {1, 2, 5}
     * @return - how many different ways we can climb the staircase with
     */
    static int solveSteps(int stepCount, int[] allowedSteps) {
        computed.clear();
        return solveStepsRecursive(stepCount, allowedSteps, 0);
    }

}
