package daily5;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily5Test {

    @Test
    void car() {
        int key = Daily5.car(Daily5.cons(3, 4));
        assertEquals(3, key);
    }

    @Test
    void cdr() {
        int value = Daily5.cdr(Daily5.cons(3, 4));
        assertEquals(4, value);
    }
}