package daily15;

import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.IntStream;

class Daily15 {
    private int counter = 0;
    private int random = 0;

    /**
     * Select a random integer from a stream with uniform probability
     * Using the Reservoir Sampling algorithm
     *
     * @param stream - input stream
     * @return - randomly chosen int from the stream
     */
    int pickRandom(IntStream stream) {
        counter = 0;
        random = 0;
        stream.forEach(this::loopBody);
        return random;
    }

    private void loopBody(int i) {
        if (counter == 0) {
            random = i;
        } else if (ThreadLocalRandom.current().nextInt(1, counter + 1) == 1) {
            random = i;
        }
        counter++;
    }
}
