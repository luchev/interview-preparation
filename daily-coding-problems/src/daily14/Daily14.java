package daily14;

import java.util.concurrent.ThreadLocalRandom;

class Daily14 {
    /**
     * Generate a random point in rectangle [xStart, xEnd] x [yStart, yEnd]
     *
     * @return random point in the given interval
     */
    private static Point generatePoint(double xStart, double xEnd, double yStart, double yEnd) {
        double x = ThreadLocalRandom.current().nextDouble(xStart, xEnd);
        double y = ThreadLocalRandom.current().nextDouble(yStart, yEnd);
        return new Point(x, y);
    }

    /**
     * Approximate Pi using Monte Carlo method
     * Approximating till the 3rd decimal place takes approximately 20 million iterations
     *
     * Iterating through the whole Integer.MAX_VALUE approximates until the 4th decimal place,
     * which can be achieved with 100 million iterations so it's useless.
     *
     * Conclusion: This algorithm is not suitable to be called every time, but instead only once to generate
     * the desired constants which are just an approximation
     *
     * Time complexity: O(2 * 10^7)
     */
    static double approximatePi() {
        int pointsInCircle = 0;
        int pointsInSquare = 0;
        Point center = new Point(0.5, 0.5);
        for (int i = 0; i < 20000000; i++) {
            Point random = generatePoint(0, 1, 0, 1);
            if (center.distanceTo(random) <= 0.5) {
                pointsInCircle++;
            } else {
                pointsInSquare++;
            }
        }
        System.out.println(pointsInCircle * 4.0 / (pointsInCircle + pointsInSquare));
        return pointsInCircle * 4.0 / (pointsInCircle + pointsInSquare);
    }

}
