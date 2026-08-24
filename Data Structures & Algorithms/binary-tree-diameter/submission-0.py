# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #dfs 
        diameter = 0

        def dfs(node):
            nonlocal diameter #modify the diameter variable in the function instead of creating a new one 

            if node is None: return 0 

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            #longest path 
            diameter = max(diameter, left_height + right_height)

            #height of subtree
            return 1 + max(left_height, right_height)
        
        dfs(root) #starting dfs/begin recursive traversal from root 
        return diameter 

