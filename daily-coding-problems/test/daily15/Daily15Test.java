package daily15;

import org.junit.jupiter.api.Test;

import java.util.stream.IntStream;

class Daily15Test {

    @Test
    void pickRandom() {
        int sum = 0;
        int samples = 100000;
        for (int i = 0; i < samples; i++) {
            IntStream stream = IntStream.range(1, 10);
            Daily15 randomPick = new Daily15();
            sum += randomPick.pickRandom(stream);
        }
        System.out.println(sum / (double)samples);
    }
}