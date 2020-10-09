# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)
# Possible memory optimization would be to serialize the tuples for each node (val,left,right) as 12 bytes (3 x 4-byte ints)

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ""

        serialized = []
        self.serialize_recursive(root, serialized)
        serialized_str = ""
        for x in serialized:
            serialized_str += ':' + "{},{},{}".format(x[0], x[1], x[2])
        return serialized_str[1:]

    def serialize_recursive(self, root: TreeNode, serialized: List[int]) -> int:
        left_child_index = -1
        if root.left:
            left_child_index = self.serialize_recursive(root.left, serialized)

        right_child_index = -1
        if root.right:
            right_child_index = self.serialize_recursive(
                root.right, serialized)

        serialized.append((root.val, left_child_index, right_child_index))
        return len(serialized) - 1

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None

        data = [x.split(',') for x in data.split(':')]
        parsed = []
        for node in data:
            parsed.append(tuple(map(lambda x: int(x), node)))

        return self.deserialize_recursive(parsed, -1)

    def deserialize_recursive(self, parsed, current_index):
        val, left_index, right_index = parsed[current_index]

        current_node = TreeNode(val)

        if left_index != -1:
            current_node.left = self.deserialize_recursive(parsed, left_index)
        if right_index != -1:
            current_node.right = self.deserialize_recursive(
                parsed, right_index)

        return current_node
