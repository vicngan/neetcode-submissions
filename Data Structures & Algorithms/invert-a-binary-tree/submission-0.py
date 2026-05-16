# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
using DFS, we can check the node parent and it's children recursively 
1: check if the root is null; if is, return None 
2: check the parent root and it's children and swap them (L-> R and R -> L)
3: go down the subnode of the parent node recursively and invert the children as well

'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: 
            return None 
        
        temp = root.left
        root.left = root.right 
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 

