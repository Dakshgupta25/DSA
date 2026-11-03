class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            twoback = 0
            oneback = arr[0]

            for i in arr[1:]:
                pick = i + twoback
                twoback = oneback
                oneback = max(pick, oneback)

            return oneback

        return max(helper(nums[:-1]), helper(nums[1:]))