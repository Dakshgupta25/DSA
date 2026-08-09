class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        j=0
        zero=0
        ans=0
        while j<len(nums):
            if nums[j]==0:
                zero+=1
            
            if zero>k:
                if ans< j-i:
                    ans=j-i
                while zero>k:
                    if nums[i]==0:
                        zero-=1
                    i+=1
            j+=1
        if zero<=k:
            ans= max(j-i,ans)
        return ans
