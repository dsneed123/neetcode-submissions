# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.swap(root)

    def swap(self, node):
        if node is None:
            return node
        temp = node.left
        node.left = node.right
        node.right = temp

        self.swap(node.left)
        self.swap(node.right)

        return node
        