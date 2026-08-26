# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #2 steps dfs; traverse every node in root as a possible starting, for each node, check if the tree root and subroot are identical 
        if subRoot is None: return True 

        if root is None: return False 

        if self.same_tree(root, subRoot): return True 

        #if not same, search left and right subtrees
        else: 
            return (self.isSubtree(root.left, subRoot ) or (self.isSubtree(root.right, subRoot)))

    def same_tree(self, node1, node2):
        #check ending (same time vs earlier)
        if node1 is None and node2 is None: return True 
        if node1 is None or node2 is None: return False 

        if node1.val == node2.val and self.same_tree(node1.left, node2.left) and self.same_tree(node1.right, node2.right):
            return True 
