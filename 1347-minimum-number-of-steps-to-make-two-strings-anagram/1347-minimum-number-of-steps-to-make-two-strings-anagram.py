class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dic1={}
        for i in s:
            dic1[i]=dic1.get(i,0)+1
        
        cnt=0
        for i in t:
            if i not in dic1 or dic1[i]==0:
                cnt+=1
            else:
                dic1[i]-=1
        return cnt