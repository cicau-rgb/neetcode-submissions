# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isIdentical(self, q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
        if q is None and p is None:
            return True

        if q is None or p is None:
            return False

        is_left_identical = self.isIdentical(q.left, p.left)
        is_right_identical = self.isIdentical(q.right, p.right)

        return q.val == p.val and is_left_identical and is_right_identical

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        return self.isIdentical(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
       



        