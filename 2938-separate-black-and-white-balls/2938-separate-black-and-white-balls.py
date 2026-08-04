class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        j=0

        for i in range(len(s)):
            if s[i]=="0":
                ans+= i-j
                j+=1
        return ans
