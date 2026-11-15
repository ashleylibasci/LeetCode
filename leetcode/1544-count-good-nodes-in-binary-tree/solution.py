# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if root == None:
            return 0
        max_num = root.val
        def getCount(root, max_num):
            nonlocal count
            if root == None:
                return
            if root.val >= max_num:
                count+=1
                max_num = root.val
            getCount(root.left, max_num)
            getCount(root.right, max_num)
        getCount(root, max_num)
        return count
        
        
