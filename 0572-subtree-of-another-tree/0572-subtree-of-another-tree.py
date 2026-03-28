# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root, otherRoot):
        if not root and not otherRoot:
            return True
        if not root or not otherRoot:
            return False
        if root.val != otherRoot.val:
            return False    
        return self.isSameTree(root.left, otherRoot.left) and self.isSameTree(root.right, otherRoot.right) 