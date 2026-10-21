# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        di = {}

        def dfs(node, level, column):
            if node:
                if level not in di:
                    di[level] = []

                di[level].append(column)

                dfs(node.left, level + 1, column * 2)
                dfs(node.right, level + 1, column * 2 + 1)

        dfs(root, 0, 0)

        return max(
            max(di[level]) - min(di[level]) + 1
            for level in di
        )