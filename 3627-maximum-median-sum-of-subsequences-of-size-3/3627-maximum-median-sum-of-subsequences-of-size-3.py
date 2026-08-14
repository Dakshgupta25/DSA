class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dsc = sorted(nums, reverse=True)
        d=1
        ans=0
        for _ in range(len(nums)//3):
            ans+=dsc[d]
            d+=2
        return ans
