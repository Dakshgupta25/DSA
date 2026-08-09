class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        
        res=[]
        for key, value in sorted(dic.items(), key=lambda x: (x[1], -x[0])):
            res+=[key]*value
        
        return res