class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.res = True

        def check(r):
            if not r:
                return 0
            left = check(r.left)
            right = check(r.right)
            if abs(left - right) > 1:
                self.res = False
            return 1 + max(left, right)

        check(root)
        return self.res
