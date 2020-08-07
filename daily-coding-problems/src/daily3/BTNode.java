package daily3;

import org.jetbrains.annotations.Contract;

class BTNode {
    private String value;
    private BTNode left = null;
    private BTNode right = null;

    @Contract(pure = true)
    BTNode(String value) {
        this.value = value;
    }

    @Contract(pure = true)
    BTNode(String value, BTNode left, BTNode right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    void setLeft(BTNode left) {
        this.left = left;
    }

    BTNode getLeft() {
        return left;
    }

    BTNode getRight() {
        return right;
    }

    void setRight(BTNode right) {
        this.right = right;
    }

    String getValue() {
        return value;
    }

    void setValue(String value) {
        this.value = value;
    }

}
