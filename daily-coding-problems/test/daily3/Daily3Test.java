package daily3;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily3Test {

    @Test
    void serialize() {
        BTNode root = new BTNode("root", new BTNode("left", new BTNode("left.left"), null), new BTNode("right"));
        Daily3 BTSerializer = new Daily3();
        String serialized = BTSerializer.serialize(root);
        assertEquals(serialized, "--root\n" + "l-left\n" + "l-left.left\n" + "up\n" + "up\n" + "r-right\n" + "up");
    }

    @Test
    void deserialize() {
        BTNode root = new BTNode("root", new BTNode("left", new BTNode("left.left"), null), new BTNode("right"));
        Daily3 BTSerializer = new Daily3();
        String serialized = BTSerializer.serialize(root);
        BTNode newRoot = BTSerializer.deserialize(serialized);
        assertEquals(newRoot.getLeft().getLeft().getValue(), "left.left");
    }
}