# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def visit(node):
            print(f'current node {node}')
            if not node:
                return node
            if node.val == p.val or node.val ==q.val:
                print('met this condition')
                return node
            #First scenario, root.val between lca, return lca
            if node.val >p.val and node.val<q.val or node.val<p.val and node.val>q.val:
                return node
            ### root.val left of tree
            if node.val >p.val and node.val >q.val:
                return visit(node.left)
            elif node.val <p.val and node.val <q.val:
                return visit(node.right)

        return visit(root)