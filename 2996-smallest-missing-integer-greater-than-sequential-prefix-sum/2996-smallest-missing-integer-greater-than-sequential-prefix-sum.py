class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += nums[i]
            else:
                break

        res = cur

        while res in nums:
            res += 1

        return res



            
