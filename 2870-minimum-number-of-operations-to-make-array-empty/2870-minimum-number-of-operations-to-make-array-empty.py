class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        res=0
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for i in dic.values():
            if i==1:
                return -1
            if i%3==0 :
                res+= i//3
            else:
                res+= (i//3)+1
        return res