class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        nums.sort(key = lambda x:x[0])
        start  = nums[0][0]
        end  = nums[0][1]
        ans = 0
        for  x in nums[1::]:
            if end < x[0]:
                ans += (end - start + 1) 
                start = x[0]

            end = max(end, x[1])
        ans += (end - start + 1) 
        return ans