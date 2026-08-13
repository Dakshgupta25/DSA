class Solution(object):
    def productExceptSelf(self, nums):
        prefix=[1]
        for i in nums[:-1]:
            prefix.append(prefix[-1]*i)
        sufix=1
        for i in range(len(nums)-1,-1,-1):
            prefix[i]*=sufix
            sufix*=nums[i]
        return prefix