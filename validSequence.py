# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkPath(self, root, arr, l, i):
        if root is None:
            return l == 0
        if (i==l-1) and (root.left == None and root.right == None) and (root.val == arr[i]):
            return True
        if (i < l) and (root.val == arr[i]):
            return (self.checkPath(root.left, arr, l, i+1) or (self.checkPath(root.right, arr, l, i+1)))
    
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        l = len(arr)
        i = 0
        return self.checkPath(root, arr, l, i)

