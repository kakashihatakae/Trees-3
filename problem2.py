# O(n)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        def helper(root_l, root_r):
            # print(root_l, root_r)
            if (not root_l) and (not root_r):
                return True
            if (root_l==None and root_r) or \
            (root_r==None and root_l):
                return False
            if root_l.val != root_r.val:
                return False
            
            return helper(root_l.left, root_r.right) and \
            helper(root_l.right, root_r.left)
        
        return helper(root.left, root.right)