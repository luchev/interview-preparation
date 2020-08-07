package daily16;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily16Test {

    @Test
    void solve() {
        CircularQueue<Integer> que = new CircularQueue<>(3);
        assertNull(que.pop());
        que.push(1);
        que.push(2);
        assertEquals(1, que.pop());
        assertEquals(2, que.pop());
        assertNull(que.pop());
        que.push(1);
        que.push(2);
        que.push(3);
        que.push(4);
        assertEquals(2, que.pop());
        assertEquals(3, que.pop());
        assertEquals(4, que.pop());
        assertNull(que.pop());
    }
}