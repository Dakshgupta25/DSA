class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        twoback=0
        oneback=nums[0]

        for i in nums[1:]:
            pick=i+twoback
            twoback=oneback
            oneback= max(pick,oneback)

        return max(oneback,twoback)