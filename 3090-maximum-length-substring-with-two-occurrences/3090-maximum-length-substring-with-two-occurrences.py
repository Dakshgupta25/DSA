class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        i=0
        j=0
        ans=0
        while j<len(s):
            dic[s[j]]=dic.get(s[j],0)+1

            while dic[s[j]]>2:
                dic[s[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
            j+=1
        return ans
