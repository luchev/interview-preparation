# Complexity(n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)
def insert(self, val):
    self.root = self.insertRecursive(self.root, val)

def insertRecursive(self, node, val):
    if node is None:
        return Node(val)
    elif val <= node.info:
        node.left = self.insertRecursive(node.left, val)
    else:
        node.right = self.insertRecursive(node.right, val)
    return node
