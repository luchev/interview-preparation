package daily20;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily20Test {

    @Test
    void getIntersection() {
        LL<Integer> a = new LL<>();
        a.add(3);
        a.add(7);
        a.add(8);
        a.add(10);

        LL<Integer> b = new LL<>();
        b.add(5);
        b.add(99);
        b.add(1);
        b.add(8);
        b.add(10);

        assertEquals(8, Daily20.getIntersection(a, b));
    }
}