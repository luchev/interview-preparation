package daily20;

class LL<T> {
    private LLNode<T> start = null;
    private LLNode<T> end = null;
    private int size = 0;

    void add(T data) {
        if (size == 0) {
            start = new LLNode<>(data);
            end = start;
        } else {
            end.setNext(new LLNode<>(data));
            end = end.getNext();
        }

        size++;
    }

    LLNode<T> getRoot() {
        return start;
    }

    int getSize() {
        return size;
    }
}
