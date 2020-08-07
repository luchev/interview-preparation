package daily10;

class TaskScheduler {
    static private int counter = 0;

    /**
     * Execute on a different thread a function after a given interval
     *
     * @param function - implements Function class with method run() which will be executed
     * @param timeout - timeout in milliseconds after which to call run()
     */
    static void createTask(Function function, int timeout) {
        Task task = new Task(function, timeout, "Thread" + counter);
        task.start();
        counter++;
    }
}
