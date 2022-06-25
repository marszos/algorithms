# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def findmin(self, root):
        curr = root 
        
        while curr.left:
            curr = curr.left
        
        return curr 
    
 
        
    
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None 
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # no children 
            if not root.left and not root.right:
                root = None 
            # 1 chilf 
            elif not root.left:
                root = root.right 
            
            elif not root.right:
                root = root.left
            
            # 2 chidren 
            else:
                temp = self.findmin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        
        return root 
      
     # https://www.youtube.com/watch?v=i2s4Tyw3_dY
     # https://leetcode.com/problems/delete-node-in-a-bst/
