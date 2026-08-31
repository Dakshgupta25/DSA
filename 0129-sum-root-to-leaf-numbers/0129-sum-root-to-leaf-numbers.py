# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        arr=[]
        def fun(roo,num):
            if roo.left==None and roo.right==None:
                arr.append(num*10+roo.val)
                return
            if roo.left:
                fun(roo.left,num*10+roo.val)
            if roo.right:
                fun(roo.right,num*10+roo.val)
        fun(root,0)
        return sum(arr)
            