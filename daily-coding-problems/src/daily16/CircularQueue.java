package daily16;

class CircularQueue<T> {
    private Object[] queue;
    private int size;
    private int front = 0;
    private int back = 0;
    private int currentItemCount = 0;

    CircularQueue(int size) {
        this.size = size;
        queue = new Object[this.size];
    }

    private void increaseBack() {
        back++;
        if (back == size) {
            back = 0;
        }
    }

    private void increaseFront() {
        front++;
        if (front == size) {
            front = 0;
        }
    }

    T pop() {
        if (currentItemCount == 0) {
            return null;
        } else {
            T copy = (T)queue[back];
            increaseBack();
            currentItemCount--;
            return copy;
        }
    }

    void push(T object) {
        queue[front] = object;
        increaseFront();
        currentItemCount++;
        if (currentItemCount > size) {
            currentItemCount--;
            increaseBack();
        }
    }

    void record(T object) {
        push(object);
    }

    T get_last(int i) {
        if (i >= currentItemCount) {
            return null;
        }
        int returnPos = (back + i) % size;
        return (T)queue[returnPos];
    }
}
