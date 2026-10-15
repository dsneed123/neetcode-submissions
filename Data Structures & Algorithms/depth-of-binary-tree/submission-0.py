# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)
        
    def height(self, head):
        if head is None:
            return 0
        
        lright = self.height(head.right)
        lleft = self.height(head.left)

        return max(lright, lleft) + 1

            

        