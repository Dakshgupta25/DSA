class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp=[-1]*len(nums)

        def fun(i):
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            if i==0:
                dp[i]=nums[i]
                return dp[i]
            pick=nums[i]+fun(i-2)
            notpick=fun(i-1)
            dp[i]=max(pick,notpick)
            return dp[i]
        return fun(len(nums)-1)