package daily7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily7Test {

    @Test
    void countDecodeVariants() {
        Daily7 decodeVariantCounter = new Daily7();
        assertEquals(2, decodeVariantCounter.countDecodeVariants("11"));
        assertEquals(3, decodeVariantCounter.countDecodeVariants("111"));
        assertEquals(5, decodeVariantCounter.countDecodeVariants("1111"));
        assertEquals(89, decodeVariantCounter.countDecodeVariants("1111111111"));
        assertEquals(10946, decodeVariantCounter.countDecodeVariants("11111111111111111111"));
    }
}