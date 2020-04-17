# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, node):
        if node is None:
            return 0;
        return 1 + max(self.height(node.left), self.height(node.right))


    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0;
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        # Get the diameter of left and irgh sub-trees 
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        return max(lheight + rheight, max(ldiameter, rdiameter)) 
