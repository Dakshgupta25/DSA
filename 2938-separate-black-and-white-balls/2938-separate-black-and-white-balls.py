class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = 0
        ans = 0
        for ch in s:
            if ch == '1':
                ones += 1
            else:
                ans += ones
        return ans