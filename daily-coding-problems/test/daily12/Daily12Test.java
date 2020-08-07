package daily12;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily12Test {

    @Test
    void solveStepsOneAndTwoSlow() {
        assertEquals(1, Daily12.solveStepsOneAndTwoSlow(1));
        assertEquals(2, Daily12.solveStepsOneAndTwoSlow(2));
        assertEquals(3, Daily12.solveStepsOneAndTwoSlow(3));
        assertEquals(5, Daily12.solveStepsOneAndTwoSlow(4));
    }

    @Test
    void solveStepsOneAndTwoFast() {
        assertEquals(1, Daily12.solveStepsOneAndTwoFast(1));
        assertEquals(2, Daily12.solveStepsOneAndTwoFast(2));
        assertEquals(3, Daily12.solveStepsOneAndTwoFast(3));
        assertEquals(5, Daily12.solveStepsOneAndTwoFast(4));
    }

    @Test
    void solveSteps() {
        assertEquals(1, Daily12.solveSteps(1, new int[] { 1, 2 }));
        assertEquals(2, Daily12.solveSteps(2, new int[] { 1, 2 }));
        assertEquals(3, Daily12.solveSteps(3, new int[] { 1, 2 }));
        assertEquals(5, Daily12.solveSteps(4, new int[] { 1, 2 }));
    }
}