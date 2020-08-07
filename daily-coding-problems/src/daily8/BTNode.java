package daily8;

class BTNode {
    private BTNode left;
    private BTNode right;
    private int value;
    private int unival = -1;

    BTNode(int value) {
        this.value = value;
    }

    int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    BTNode getRight() {
        return right;
    }

    void setRight(BTNode right) {
        this.right = right;
    }

    BTNode getLeft() {
        return left;
    }

    void setLeft(BTNode left) {
        this.left = left;
    }

    int getUnival() {
        return unival;
    }

    void setUnival(int unival) {
        this.unival = unival;
    }
}
