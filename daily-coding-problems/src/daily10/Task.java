package daily10;


public class Task implements Runnable {
    private Thread thread;
    private String threadName;
    private int timeoutMilliseconds;
    private Function toRun;

    Task(Function toRun, int timeoutMilliseconds, String threadName) {
        this.toRun = toRun;
        this.timeoutMilliseconds = timeoutMilliseconds;
        this.threadName = threadName;
    }

    @Override
    public void run() {
        try {
            Thread.sleep(timeoutMilliseconds);
            toRun.run();
        } catch (InterruptedException e) {
            System.out.println("Thread " + threadName + " interrupted");
        }
    }

    void start() {
        if (this.thread == null) {
            this.thread = new Thread(this, threadName);
            this.thread.start();
        }
    }
}
