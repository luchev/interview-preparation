package daily2;

import org.junit.jupiter.api.Test;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class Daily2Test {

    @Test
    void solve() {
        ArrayList<Integer> input = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        ArrayList<Integer> expectedOutput = new ArrayList<>(Arrays.asList(120, 60, 40, 30, 24));
        ArrayList<Integer> output = Daily2.solve(input);
        assertEquals(output, expectedOutput);
    }
}