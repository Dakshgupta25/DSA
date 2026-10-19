class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand=0
        cnt=0
        for i in nums:
            if cnt==0:
                cand=i
                cnt=1
            elif i==cand:
                cnt+=1
            else:
                cnt-=1
        return cand