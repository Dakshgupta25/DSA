class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp={}
        for i in range(len(nums)):
            if target-nums[i] in mp:
                return [mp[target-nums[i]],i]
            if nums[i] not in mp:
                mp[nums[i]]=i
        
            
            