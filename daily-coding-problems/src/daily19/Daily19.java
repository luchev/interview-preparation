package daily19;

import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.Comparator;

class Daily19 {
    /**
     * Solution for The Colorful Street problem
     *
     * Complexity (n = number of houses, k = number of colors)
     * Time complexity: O(n * k)
     * Space complexity: O(1)
     *
     * @param costs - matrix NxK for N houses with the prices for K different colors
     * @return - the minimum cost for painting all houses such that no 2 neighbouring houses are of the same color
     */
    static int solve(int[][] costs) {
        if (costs[0].length < 2) {
            return -1;
        } else if (costs[0].length == 2) {
            return solveTwoColors(costs);
        } else {
            return solveThreeOrMoreColors(costs);
        }
    }

    /**
     * Solve the colorful street problem with 3 or more colors
     *
     * @param costs - matrix with costs
     * @return - the minimum cost
     */
    private static int solveThreeOrMoreColors(int[][] costs) {
        ArrayList<ArrayList<Integer>> indexesToCheck;
        if (costs[0].length > 3) {
            indexesToCheck = reduceColors(costs);
        } else {
            indexesToCheck = firstThreeIndices(costs.length);
        }

        return solveThreeColors(costs, indexesToCheck);
    }

    /**
     * We generate a matrix with 'length'-number of rows like this one [ 0, 1, 2 ]
     * Used to make the algorithm more generic for solving problems of size 3 <=
     *
     * @param length - how big the matrix needs to be length x 3
     * @return - matrix of size 3 x length with rows like this one [ 0, 1, 2 ]
     */
    private static ArrayList<ArrayList<Integer>> firstThreeIndices(int length) {
        ArrayList<ArrayList<Integer>> costIndices = new ArrayList<>();

        for (int i = 0; i < length; i++) {
            costIndices.add(new ArrayList<>());
            costIndices.get(0).add(0);
            costIndices.get(0).add(1);
            costIndices.get(0).add(2);
        }

        return costIndices;
    }

    /**
     * Reduce the NxK matrix problem to Nx3 which is simpler to solve
     *
     * @param costs - matrix with all costs
     * @return - array of array[3] with indices of the indices of the cheapest 3 colors
     */
    private static ArrayList<ArrayList<Integer>> reduceColors(int[][] costs) {
        ArrayList<ArrayList<Integer>> costIndices = new ArrayList<>();

        for (int[] cost : costs) {
            costIndices.add(smallestThree(cost));
        }

        return costIndices;
    }

    /**
     * Get the 3 smallest cost indices from a list of numbers
     * @param numbers - an array of numbers
     * @return - array of 3 indices of the smallest numbers in the array
     */
    private static ArrayList<Integer> smallestThree(int[] numbers) {
        ArrayList<AbstractMap.SimpleEntry<Integer, Integer>> firstThree = new ArrayList<>();
        firstThree.add(new AbstractMap.SimpleEntry<>(0, numbers[0]));
        firstThree.add(new AbstractMap.SimpleEntry<>(1, numbers[1]));
        firstThree.add(new AbstractMap.SimpleEntry<>(2, numbers[2]));
        firstThree.sort(Comparator.comparing(AbstractMap.SimpleEntry::getValue));

        int[] result = new int[] {firstThree.get(0).getKey(), firstThree.get(1).getKey(), firstThree.get(2).getKey()};

        for (int i = 3; i < numbers.length; i++) {
            if (numbers[i] <= numbers[result[0]]) {
                result[2] = result[1];
                result[1] = result[0];
                result[0] = i;
            } else if (numbers[i] < numbers[result[2]]) {
                if (numbers[i] < numbers[result[1]]) {
                    result[2] = result[1];
                    result[1] = i;
                } else {
                    result[2] = i;
                }
            }
        }

        ArrayList<Integer> arrayListResult = new ArrayList<>();
        arrayListResult.add(result[0]);
        arrayListResult.add(result[1]);
        arrayListResult.add(result[2]);

        return arrayListResult;
    }

    /**
     * Given we have N houses with 3 colors solve the problem by going through all routes for coloring
     *
     * @param costs - matrix with all costs
     * @param indices - a list of list[3] chosen minimum prices
     * @return - the minimum cost required to paint all N houses with no 2 neighbouring houses of the same color
     */
    private static Integer solveThreeColors(int[][] costs, ArrayList<ArrayList<Integer>> indices) {
        orderIndices(indices);

        int prev0 = costs[0][indices.get(0).get(0)];
        int prev1 = costs[0][indices.get(0).get(1)];
        int prev2 = costs[0][indices.get(0).get(2)];

        int accumulator0 = 0;
        int accumulator1 = 0;
        int accumulator2 = 0;

        for (int i = 1; i < costs.length; i++) {
            accumulator0 = costs[i][indices.get(i).get(0)] + Math.min(prev1, prev2);
            accumulator1 = costs[i][indices.get(i).get(1)] + Math.min(prev0, prev2);
            accumulator2 = costs[i][indices.get(i).get(2)] + Math.min(prev0, prev1);

            prev0 = accumulator0;
            prev1 = accumulator1;
            prev2 = accumulator2;
        }

        return Math.min(Math.min(accumulator0, accumulator1), accumulator2);
    }

    /**
     * @param array - array whose items to swap
     * @param i - first pos to swap
     * @param j - second position to swap
     */
    private static void swap(ArrayList<Integer> array, int i, int j) {
        int temp = array.get(i);
        array.set(i, array.get(j));
        array.set(j, temp);
    }

    /**
     * Order a Nx3 matrix
     * Ordering rules:
     * if row I and row I + 1 contain the same number these numbers must be one under the other
     * so for example
     * [ 1, 2 ]
     * [ 0, 1 ]
     * becomes
     * [ 1, 2 ]
     * [ 1, 0 ]
     * as we move the 1s to be under each other
     * @param indices - a Nx3 matrix to be ordered
     */
    private static void orderIndices(ArrayList<ArrayList<Integer>> indices) {
        for (int i = 1; i < indices.size(); i++) {
            int indexZero = indices.get(i).indexOf(indices.get(i - 1).get(0));
            if (indexZero >= 0) {
                swap(indices.get(i), indexZero, 0);
            }

            int indexOne = indices.get(i).indexOf(indices.get(i - 1).get(1));
            if (indexOne >= 0) {
                swap(indices.get(i), indexOne, 1);
            }

            int indexTwo = indices.get(i).indexOf(indices.get(i - 1).get(2));
            if (indexTwo >= 0) {
                swap(indices.get(i), indexTwo, 2);
            }
        }
    }

    /**
     * With 2 colors brute force the solution trying the 2 possible alternatives
     * it's either
     * 1 0 1 0
     * or
     * 0 1 0 1
     *
     * @param costs - array of N rows, 2 columns
     * @return - the array with minimum alternating sum
     */
    private static int solveTwoColors(int[][] costs) {
        int sumStartWithColorZero = 0;
        int sumStartWithColorOne = 0;

        for (int i = 0; i < costs.length; i++) {
            if ((i & 1) == 1) {
                sumStartWithColorZero += costs[i][0];
                sumStartWithColorOne += costs[i][1];
            } else {
                sumStartWithColorZero += costs[i][1];
                sumStartWithColorOne += costs[i][0];
            }
        }

        return Math.min(sumStartWithColorOne, sumStartWithColorZero);
    }
}
