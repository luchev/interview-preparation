package daily10;

class Daily10 {
    static void solve() {
        // Create 2 functions and execute them after 2s and 1s, One should finish before Two
        Function one = new Function("One");
        Function two = new Function("Two");
        TaskScheduler.createTask(two, 2000);
        TaskScheduler.createTask(one, 1000);
        // Simulate long running program in the main thread
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            System.out.println("Main thread interrupted");
        }
    }
}
