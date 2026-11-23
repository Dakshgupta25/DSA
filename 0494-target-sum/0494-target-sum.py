class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)

        dp={}
        def solve(ind,cur):
            if ind==n-1:
                if cur-nums[n-1]==target and cur+nums[n-1]==target:
                    return 2
                elif cur-nums[n-1]==target or cur+nums[n-1]==target:
                    return 1
                else:
                    return 0
            if (ind,cur) in dp:
                return dp[(ind,cur)]
            a=solve(ind+1,cur+nums[ind])
            s=solve(ind+1,cur-nums[ind])
            dp[(ind,cur)]=a+s
            return dp[(ind,cur)]
        return solve(0,0)