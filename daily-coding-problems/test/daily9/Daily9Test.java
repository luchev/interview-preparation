package daily9;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily9Test {


    @Test
    void maxSum() {
        assertEquals(13, Daily9.maxSum(new int[] { 2, 4, 6, 2, 5 }));
        assertEquals(10, Daily9.maxSum(new int[] { 5, 1, 1, 5 }));
        assertEquals(10, Daily9.maxSum(new int[] { 1, 0, 3, 9, 2 }));
        assertEquals(3, Daily9.maxSum(new int[] { -2, -3, -1, 1, 3, 1 }));
    }
}