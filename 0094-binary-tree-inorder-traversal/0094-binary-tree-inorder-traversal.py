# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        def inorder(r):
            if not r:
                return
            inorder(r.left)
            res.append(r.val)
            inorder(r.right)
        inorder(root)
        return res

