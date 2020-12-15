# Complexity(n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    que = []
    que.append(root)
    while len(que) > 0:
        node = que.pop(0)
        if node is None:
            continue
        print(node.info, end=' ')
        que.append(node.left)
        que.append(node.right)
