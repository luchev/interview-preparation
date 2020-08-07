package daily13;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily13Test {

    @Test
    void solve() {
        assertEquals(0, Daily13.solve("abcba", 0));
        assertEquals(1, Daily13.solve("abcba", 1));
        assertEquals(3, Daily13.solve("abcba", 2));
        assertEquals(4, Daily13.solve("bbbb", 1));
        assertEquals(3, Daily13.solve("bbaccc", 1));
    }
}