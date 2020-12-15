# Complexity(n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root.left is not None and root.right is not None:
        return 1 + max(height(root.left), height(root.right))
    elif root.left is not None:
        return 1 + height(root.left)
    elif root.right is not None:
        return 1 + height(root.right)
    else:
        return 0
