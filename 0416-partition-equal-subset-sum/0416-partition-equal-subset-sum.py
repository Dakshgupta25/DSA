class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2 != 0:
            return False

        k = total // 2

        # Base case
        prev = [False] * (k + 1)
        prev[0] = True

        if nums[0] <= k:
            prev[nums[0]] = True

        for ind in range(1, len(nums)):
            cur = [False] * (k + 1)

            # Target 0 is always possible
            cur[0] = True

            for target in range(1, k + 1):

                # Not take current element
                notTake = prev[target]

                # Take current element
                take = False
                if nums[ind] <= target:
                    take = prev[target - nums[ind]]

                cur[target] = take or notTake

            prev = cur

        return prev[k]