class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        heapq.heapify(nums)
        arr=[]
        while nums:
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            arr.append(b)
            arr.append(a)
        return arr