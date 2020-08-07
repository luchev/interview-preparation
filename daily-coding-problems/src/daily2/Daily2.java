package daily2;

import java.util.ArrayList;

class Daily2 {
    /**
     * Loop through all the numbers multiplying them in product
     * Loop through all the numbers and add to the new array product/input(i)
     *
     * Complexity (n = size of input):
     * Time complexity: O(n)
     * Space complexity: O(n)
     *
     * Potential problems:
     * Overflow of the product
     *
     * @param numbers - array of numbers
     * @return numbers where each position I is the product of all numbers from the input except the Ith number
     */
    static ArrayList<Integer> solve(ArrayList<Integer> numbers) {
        ArrayList<Integer> multiplied = new ArrayList<>();
        int product = 1;
        for (int i : numbers) {
            product *= i;
        }
        for (int i : numbers) {
            int productI = product / i;
            multiplied.add(productI);
        }
        return multiplied;
    }
}
