package daily8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily8Test {

    @Test
    void countUniversalTrees() {
        BTNode root = new BTNode(0);
        root.setLeft(new BTNode(1));
        root.setRight(new BTNode(0));
        root.getRight().setRight(new BTNode(0));
        root.getRight().setLeft(new BTNode(1));
        root.getRight().getLeft().setLeft(new BTNode(1));
        root.getRight().getLeft().setRight(new BTNode(1));

        Daily8 solver = new Daily8();
        assertEquals(5, solver.countUniversalTrees(root));
    }
}