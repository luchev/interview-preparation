package daily1;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class Daily1Test {

    @Test
    void solve() {
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(10, 15, 3, 7));
        boolean test = Daily1.solve(numbers, 17);
        assertTrue(test);
    }
}