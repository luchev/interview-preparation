package daily20;

class LLNode<T> {
    private T data = null;
    private LLNode<T> next = null;

    LLNode() { }

    LLNode(T data) {
        this.data = data;
    }

    T getData() {
        return data;
    }

    void setData(T data) {
        this.data = data;
    }

    LLNode<T> getNext() {
        return next;
    }

    void setNext(LLNode<T> next) {
        this.next = next;
    }
}
