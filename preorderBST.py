# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: 
            return None
        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder([val for val in preorder if val < preorder[0]])
        root.right = self.bstFromPreorder([val for val in preorder if val > preorder[0]])
        return root