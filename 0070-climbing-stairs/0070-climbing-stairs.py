class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        f=1
        s=2
        for i in range(3,n+1):
            temp=f+s
            f=s
            s=temp
        return s

        