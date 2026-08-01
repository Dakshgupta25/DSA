class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        cnt1 = nums1.count(0)
        cnt2 = nums2.count(0)

        # Minimum possible sums after replacing every 0 with at least 1
        minSum1 = sum1 + cnt1
        minSum2 = sum2 + cnt2

        target = max(minSum1, minSum2)

        # If an array has no zeros, its sum cannot be increased
        if cnt1 == 0 and sum1 < target:
            return -1

        if cnt2 == 0 and sum2 < target:
            return -1

        return target