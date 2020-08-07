package daily18;

import org.junit.jupiter.api.Test;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class Daily18Test {

    @Test
    void solve() {
        Daily18 solver = new Daily18();
        ArrayList<Integer> output = solver.solve(new int[] { 10, 5, 2, 7, 8, 7 }, 3);
        ArrayList<Integer> expectedOutput = new ArrayList<Integer>(Arrays.asList(10, 7, 8, 8 ));
        assertEquals(expectedOutput, output);
    }
}