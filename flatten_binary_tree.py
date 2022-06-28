# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.flatten(root.left)
            self.flatten(root.right)
            
            if root.left is not None:
                current = root.left
                
                while current.right:
                    current = current.right 
                current.right = root.right 
                root.right = root.left 
                root.left = None 
        
        return root
     
    
    # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
    # https://www.youtube.com/watch?v=pduCoCDpZMg
