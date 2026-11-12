class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def atMost(goal):
            if goal < 0:
                return 0
            
            i = 0
            cur = 0
            res = 0
            
            for j in range(len(nums)):
                cur += nums[j]
                
                while cur > goal:
                    cur -= nums[i]
                    i += 1
                
                res += j - i + 1
            
            return res
        
        return atMost(goal) - atMost(goal-1)    