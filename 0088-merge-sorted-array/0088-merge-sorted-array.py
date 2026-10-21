class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        x=n+m-1
        n-=1
        m-=1
        while m>=0 and n>=0 and x>=0:
            if nums1[m]>=nums2[n]:
                nums1[x]=nums1[m]
                m-=1
            else:
                nums1[x]=nums2[n]
                n-=1
            x-=1
        while m>=0 and x>=0:
            nums1[x]=nums1[m]
            m-=1
            x-=1
        while n>=0 and x>=0:
            nums1[x]=nums2[n]
            n-=1
            x-=1
