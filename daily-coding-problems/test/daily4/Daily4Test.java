package daily4;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily4Test {
    // [3, 4, -1, 1] -> 2
    // [1, 2, 0] -> 3
    // [4, 3, 2, 1] -> 5
    // [-1, -2, 0] -> 1
    @Test
    void solve() {
        assertEquals(2, Daily4.solve(new int[]{3, 4, -1, 1}));
        assertEquals(3, Daily4.solve(new int[]{0, 1, 2}));
        assertEquals(5, Daily4.solve(new int[]{4, 3, 2, 1}));
        assertEquals(1, Daily4.solve(new int[]{-1, -2, 0}));
    }
}