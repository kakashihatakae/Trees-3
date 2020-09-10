# Runtime O(n)

# Here I try to a backtracking approach. I maintain a global curent 
# array. I add element as it moves downwards in the list. I pop elements 
# from it as it moves upwards in the tree.
# I add a copy of the current list in ht ans ans list and 
# then I return this ans list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        current = []
        ans = []
        
        def helper(root, summ):
            if root == None:
                return
            
            current.append(root.val)
            summ += root.val
            if not root.left and not root.right and summ == sum:
                ans.append(current.copy())
            helper(root.left, summ)
            helper(root.right, summ)
            current.pop()
        helper(root, 0)
        return ans