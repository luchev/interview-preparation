package daily8;

class Daily8 {
    /**
     * Counter for unival subtrees
     */
    private int count = 0;

    /**
     * If the left tree is not checked for unival - check it
     * If the right tree is not checked for unival - check it
     *
     * If the tree has no children - root is unival
     * If the tree has one child and it's unival - root is unival
     * If the tree has two children which are both unival and have the same value - root is unival
     * In all other cases root is not unival
     *
     * Complexity (n = number of nodes in tree):
     * Time complexity: O(n)
     * Space complexity: O(height of tree) on the stack
     *
     * @param root - node in a binary tree/subtree
     */
    private void generateUnival(BTNode root) {
        if (root.getLeft() != null && root.getLeft().getUnival() == -1) {
            generateUnival(root.getLeft());
        }
        if (root.getRight() != null && root.getRight().getUnival() == -1) {
            generateUnival(root.getRight());
        }

        if (root.getLeft() == null && root.getRight() == null) {
            root.setUnival(1);
        } else if (root.getLeft() != null && root.getRight() == null) {
            if (root.getLeft().getUnival() == 1) {
                root.setUnival(1);
            } else {
                root.setUnival(0);
            }
        } else if (root.getLeft() == null && root.getRight() != null) {
            if (root.getRight().getUnival() == 1) {
                root.setUnival(1);
            } else {
                root.setUnival(0);
            }
        } else {
            if (root.getLeft().getUnival() == 1 && root.getRight().getUnival() == 1 &&
                    root.getLeft().getValue() == root.getRight().getValue()) {
                root.setUnival(1);
            } else {
                root.setUnival(0);
            }
        }
    }

    /**
     * Count the number of unival subtrees after having generated them
     *
     * Complexity (n = number of nodes in tree):
     * Time complexity: O(n)
     * Space complexity: O(height of tree) on the stack
     *
     * @param root - node in a binary tree/subtree
     */
    private void countUnival(BTNode root) {
        if (root.getUnival() == 1) {
            count++;
        }
        if (root.getLeft() != null) {
            countUnival(root.getLeft());
        }
        if (root.getRight() != null) {
            countUnival(root.getRight());
        }
    }

    /**
     * Clear a tree from it's unival values as it may be changed and invalid
     *
     * Complexity (n = number of nodes in tree):
     * Time complexity: O(n)
     * Space complexity: O(height of tree) on the stack
     *
     * @param root - node in a binary tree/subtree
     */
    private void clearUnival(BTNode root) {
        root.setUnival(-1);

        if (root.getLeft() != null) {
            clearUnival(root.getLeft());
        }
        if (root.getRight() != null) {
            clearUnival(root.getRight());
        }
    }

    /**
     * Complexity (n = number of nodes in tree):
     * Time complexity: O(n)
     *
     * @param root - root of a binary tree to count its unival subtrees
     * @return - number of unival subtrees
     */
    int countUniversalTrees(BTNode root) {
        count = 0;
        clearUnival(root);
        generateUnival(root);
        countUnival(root);
        return count;
    }
}
