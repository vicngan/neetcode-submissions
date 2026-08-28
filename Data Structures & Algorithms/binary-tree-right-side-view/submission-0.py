# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs (node, depth):
            if not node: 
                return 

            if depth == len(res): #depth = curr node level, res store 1 visible value per level; len(res) = number of level already recorded, when these equal, that means that we have reach this depth for the first time and curr node added  
                res.append(node.val)
            
            #explore right first, go down each depth by 1 
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root,0)
        return res 