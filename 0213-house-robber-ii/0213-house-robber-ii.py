class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n == 1:
            return nums[0]

        def helper(start, end):
            twoback = 0
            oneback = 0

            for i in range(start, end):
                pick = nums[i] + twoback
                twoback = oneback
                oneback = max(pick, oneback)

            return oneback

        return max(helper(0, n-1), helper(1, n))