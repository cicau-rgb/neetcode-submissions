# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertSubTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None:
            return node

        self.invertSubTree(node.left)
        self.invertSubTree(node.right)

        tmp = node.left
        node.left = node.right
        node.right = tmp

        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        self.invertSubTree(root.left)
        self.invertSubTree(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root

    




        

        