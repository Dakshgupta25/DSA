class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n

        # Find the index of the minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Ensure left_idx is smaller and right_idx is larger
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Scenario 1: Delete only from the front
        opt1 = right + 1

        # Scenario 2: Delete only from the back
        opt2 = n - left

        # Scenario 3: Delete from both front and back
        opt3 = (left + 1) + (n - right)

        return min(opt1, opt2, opt3)