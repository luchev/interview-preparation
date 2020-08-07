package daily1;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

abstract class Daily1 {
    /**
     * First number read is how many numbers will be in the list
     * Then read said numbers with a for loop
     * ReadFromStdin 1 more number in the for loop - it's the number K from the problem
     * K is the last number in the list
     */
    private ArrayList<Integer> readFromStdin() {
        ArrayList<Integer> list = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        int count = in.nextInt();
        for (int i = 0; i < count + 1; i++) {
            list.add(in.nextInt());
        }
        return list;
    }

    /**
     * ReadFromStdin all numbers from the input
     * K is the last number in the list, remove it
     */
    void runSolve() {
        ArrayList<Integer> numbers = readFromStdin();
        if (numbers.size() < 3) {
            throw new  IllegalArgumentException("Not enough arguments");
        }

        int desiredSum =  numbers.remove(numbers.size() - 1);
        System.out.println("Number of integers: " + numbers.size());
        System.out.println("Looking for sum: " + desiredSum);

        solve(numbers, desiredSum);
    }
    /**
     * If the numbers are within limited range it can be solved linearly
     * with time and space complexity O(largest number)
     *
     * Sort the list to apply efficient search
     * Try with the smallest and largest numbers first
     * If their sum = K, we're done
     * If their sum < K then we need a bigger number in the sum
     * If their sum > K then we need smaller number in the sum
     * Repeat until sum = K or until all numbers are checked
     *
     * Complexity (n = size of input):
     * O(n) for input
     * O(n*log(n)) for sorting
     * O(n) for search from both sides, reducing the counter by 1 each time (either from the left or the right)
     * Final time complexity: O(n*log(n))
     * Final space complexity: O(n)
     *
     * @param numbers - input array of numbers
     * @param desiredSum - look if 2 numbers from the array add up to this sum
     * @return true if 2 numbers from the array add up to desiredSum, false otherwise
     */
    static boolean solve(ArrayList<Integer> numbers, int desiredSum) {
        Collections.sort(numbers);
        int start = 0;
        int end = numbers.size() - 1;
        while(start != end) {
            int sum = numbers.get(start) + numbers.get(end);
            if (sum == desiredSum) {
                System.out.println("Found " + numbers.get(start) + " + " + numbers.get(end) + " = " + desiredSum);
                return true;
            }
            else if (sum > desiredSum) {
                end--;
            }
            else {
                start++;
            }
        }
        System.out.println("No numbers in the list add up to " + desiredSum);
        return false;
    }
}
