# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def visit(node):
            if node is None:
                return None
            if node.left:
                visit(node.left)
            output.append(node.val)
            if node.right:
                visit(node.right)
            
        visit(root)
        return output
            