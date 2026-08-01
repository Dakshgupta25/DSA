class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        i=0
        j=0
        res=0
        while j<len(s):
            while j<len(s) and s[j] not in s[i:j]:
                j+=1
            if j<len(s):
                res+=1
            i=j
            j+=1
        return res+1
