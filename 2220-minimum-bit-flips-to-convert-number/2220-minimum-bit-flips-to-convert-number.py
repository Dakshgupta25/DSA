class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        x=start^goal
        cnt=0
        while x:
            if (x&1)==1:
                cnt+=1
            x=x>>1
        return cnt