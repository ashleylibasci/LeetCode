# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def findPath(node, remaining):
            if node is None:
                return 0
            count = 0
            if node.val == remaining:
                count += 1
            remaining -= node.val
            count = count + findPath(node.left, remaining)+ findPath(node.right, remaining)
            return count
        def explore(node):
            if node is None:
                return 0
            paths = findPath(node, targetSum)
            paths += explore(node.left)
            paths+= explore(node.right)
            return paths
        return explore(root)
            
             
        
