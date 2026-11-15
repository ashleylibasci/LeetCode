# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        root_1_seq = []
        root_2_seq = []
        def getLeaves(root, seq):
            if root is None:
                return
            if root.left == None and root.right == None:
                seq.append(root.val)
                return
            getLeaves(root.left, seq)
            getLeaves(root.right, seq)
        getLeaves(root1, root_1_seq)
        getLeaves(root2,root_2_seq)
        return root_1_seq == root_2_seq
            
            
        
        
