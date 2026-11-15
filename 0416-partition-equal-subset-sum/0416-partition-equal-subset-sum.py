class Solution(object):
    def canPartition(self, nums):
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        k = total // 2
        memo=[[-1]*n for _ in range(k+1)]
        def solve(ind, target):
            if target == 0:
                return True

            if ind == 0:
                return nums[0] == target
            if memo[target][ind]!=-1:
                return memo[target][ind]

            notTake = solve(ind-1, target)

            take = False
            if nums[ind] <= target:
                take = solve(ind-1, target-nums[ind])

            memo[target][ind]= take or notTake
            return memo[target][ind]
        return solve(n-1,k)