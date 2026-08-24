# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None: return True, 0 
            #empty subtree = balanced

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            #requirements for balance
            balanced = (left_balanced and right_balanced and abs(left_height - right_height) <= 1) #left and right subtree must be balanced and the curr node subtree height can differ by at most 1

            height = 1 + max(left_height, right_height)

            return balanced, height
        
        return dfs(root)[0]
        #return 2 vals and [0] accesses the first value (balance)
                
        