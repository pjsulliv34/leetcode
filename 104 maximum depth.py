# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

    #depth first,
    #    def visit(node):
    #     if not node:
    #         return 0
    #     print('running')
    #     return 1 + max(visit(node.left),visit(node.right))
    #    return visit(root)

        #breadth first

        queue = [root]
        depth = 0 
        if not root:
            return 0
        while len(queue)>0:
            depth +=1
            q_n = []
            while queue:
                item = queue.pop()
                if item and item.left:
                    q_n.append(item.left)
                if item and item.right:
                    q_n.append(item.right)
            queue.extend(q_n)
        return depth
