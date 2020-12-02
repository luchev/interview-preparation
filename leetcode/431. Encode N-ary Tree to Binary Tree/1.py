# Complexity (n = nodes in the tree, h = height of the tree)
# Time complexity: O(n)
# Space complexity: O(h)

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if root is None:
            return None

        encodedRoot = TreeNode(root.val)
        if len(root.children) > 0:
            encodedRoot.right = self.encode(root.children[0])

        child = encodedRoot.right
        for i in range(1, len(root.children)):
            child.left = self.encode(root.children[i])
            child = child.left

        return encodedRoot

	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if data is None:
            return None

        decodedRoot = Node(data.val, [])

        child = data.right
        while child:
            decodedRoot.children.append(self.decode(child))
            child = child.left

        return decodedRoot
