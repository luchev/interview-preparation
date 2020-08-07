package daily3;

import java.security.InvalidParameterException;
import java.util.EmptyStackException;
import java.util.Stack;

class Daily3 {
    private StringBuilder serializedBT;

    /**
     * Pre-order traversal for serializing BTree
     * @param root - the current node which to serialize
     */
    private void serializeRecursive(BTNode root) {
        serializedBT.append(root.getValue());
        serializedBT.append("\n");

        if (root.getLeft() != null) {
            serializedBT.append("l-");
            serializeRecursive(root.getLeft());
        }
        if (root.getRight() != null) {
            serializedBT.append("r-");
            serializeRecursive(root.getRight());
        }

        serializedBT.append("up\n");
    }

    /**
     * Serialize a BTree to string
     * Lines starting with:
     * -- mean change current node value (used for root)
     * r-VALUE mean add right node with value = VALUE
     * l-VALUE mean add left node with value = VALUE
     * up mean move to the parent node
     *
     * Algorithm used Pre-order traversal (
     *
     * Complexity (n = number of nodes in the tree):
     * Time complexity: O(n)
     *
     * @param root - the root of the BTree to serialize
     * @return serialized BTree to string
     */
    String serialize(BTNode root) {
        serializedBT = new StringBuilder();
        serializedBT.append("--"); // Add special root symbol at the start
        serializeRecursive(root);
        return serializedBT.substring(0, serializedBT.length() - 4);
    }

    /**
     * Deserialize a BTree from string
     *
     * Parse each line as it represents either adding a new right or left node (r- or l-)
     * or going up to the parent (up)
     * or changing the current node value (--)
     *
     * To achieve going up we keep a stack with parents
     *
     * Complexity (n = string length)
     * Read string once to split it in lines O(n)
     * Parse each line O(n)
     * Final time complexity: O(n)
     *
     * @param string - serialized BTree
     * @return the root of the deserialized BTree
     */
    BTNode deserialize(String string) {
        BTNode root = new BTNode("");
        Stack<BTNode> parents = new Stack<>();
        String[] lines = string.split("\n");
        for (String line : lines) {
            if (line.startsWith("--")) { // Special line for changing root value
                root.setValue(line.substring(2));
            } else if (line.startsWith("up")) { // Go up to the parent
                try {
                    root = parents.pop();
                } catch (EmptyStackException exception) {
                    throw new InvalidParameterException("The string is not a serialized BTree");
                }
            } else if (line.startsWith("l-")) { // Make a left node and move to it
                root.setLeft(new BTNode(line.substring(2)));
                parents.push(root);
                root = root.getLeft();
            } else if (line.startsWith("r-")) { // Make a right node and move to it
                root.setRight(new BTNode(line.substring(2)));
                parents.push(root);
                root = root.getRight();
            } else {
                throw new InvalidParameterException("The string is not a serialized BTree");
            }
        }
        return root;
    }
}
