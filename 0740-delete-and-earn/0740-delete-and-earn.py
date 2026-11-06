class Solution:
    def deleteAndEarn(self, nums):
        points = [0] * (max(nums) + 1)

        for num in nums:
            points[num] += num

        prev2 = 0
        prev1 = 0

        for point in points:
            current = max(prev1, prev2 + point)
            prev2 = prev1
            prev1 = current

        return prev1