class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n=len(t)
        j=0
        for i in s:
            if j>=n:
                break
            if i==t[j]:
                j+=1
        return n-j
        