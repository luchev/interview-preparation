package daily9;

import java.util.HashMap;

class Daily9 {
    private static HashMap<Integer, Integer> memoization = new HashMap<>();

    private static int maxSumRecursive(int[] array, int i) {
        if (i == 0) {
            return Math.max(0, array[0]);
        }
        if (i == 1) {
            return Math.max(0, Math.max(array[0], array[1]));
        }

        if (memoization.containsKey(i)) {
            return memoization.get(i);
        }
        int current = Math.max(maxSumRecursive(array, i - 1), array[i] + maxSumRecursive(array, i - 2));
        memoization.put(i, current);
        return current;
    }

    static int maxSum(int[] array) {
        memoization.clear();
        return maxSumRecursive(array, array.length - 1);
    }
}
