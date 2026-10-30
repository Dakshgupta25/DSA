# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.res=root.val

        def fun(r):
            
            if not r:
                return 0
            
            left= max(0,fun(r.left))
            right=max(0,fun(r.right))

            if self.res< r.val+left+right:
                self.res= r.val+left+right
            
            return max(left+r.val,right+r.val)
        
        fun(root)
        return self.res