package daily19;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily19Test {

    @Test
    void solver() {
        int[][] costs4colors = new int[4][];
        costs4colors[0] = new int[] {1, 2, 3, 4};
        costs4colors[1] = new int[] {1, 2, 1, 0};
        costs4colors[2] = new int[] {6, 1, 1, 5};
        costs4colors[3] = new int[] {2, 3, 5, 4};
        assertEquals(4, Daily19.solve(costs4colors));

        int[][] costs2colors = new int[4][];
        costs2colors[0] = new int[] {1, 5};
        costs2colors[1] = new int[] {5, 1};
        costs2colors[2] = new int[] {1, 5};
        costs2colors[3] = new int[] {5, 1};

        assertEquals(4, Daily19.solve(costs2colors));
    }
}