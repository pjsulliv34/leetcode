class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def visit(root):
            print(f'current root {root}')
            print(f'val {val}')
            if root == None:
                return None
            if val == root.val:
                return root
            if val < root.val:
                return visit(root.left)
            if val > root.val:
                return visit(root.right)

        return visit(root)
        