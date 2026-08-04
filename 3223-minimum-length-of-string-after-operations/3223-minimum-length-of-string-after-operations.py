class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
            if dic[i]==3:
                dic[i]-=2
        return sum(dic.values())