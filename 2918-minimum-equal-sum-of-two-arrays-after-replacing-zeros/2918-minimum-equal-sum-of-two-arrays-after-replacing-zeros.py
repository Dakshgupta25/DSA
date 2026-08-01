class Solution(object):
    def minSum(self, nums1, nums2):
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        cnt1 = nums1.count(0)
        cnt2 = nums2.count(0)

        min1 = sum1 + cnt1
        min2 = sum2 + cnt2

        if min1 == min2:
            return min1

        if min1 > min2:
            if cnt2 == 0:
                return -1
            return min1

        if cnt1 == 0:
            return -1
        return min2