class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        cur=0
        for i in nums:
            cur+=i
            res=max(res,cur)
            if cur<0:
                cur=0
        return res