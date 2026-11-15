class Solution(object):
    def canPartition(self, nums):
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        k = total // 2
        memo=[[-1]*(k+1) for _ in range(n)]
        def solve(ind, target):
            if target == 0:
                return True

            if ind == 0:
                return nums[0] == target
            if memo[ind][target]!=-1:
                return memo[ind][target]

            notTake = solve(ind-1, target)

            take = False
            if nums[ind] <= target:
                take = solve(ind-1, target-nums[ind])

            memo[ind][target]= take or notTake
            return memo[ind][target]
        return solve(n-1,k)