class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        maxheap=[-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            a=-heapq.heappop(maxheap)
            b=-heapq.heappop(maxheap)
            if a!=b:
                heapq.heappush(maxheap,-abs(a-b))
        if maxheap:
            return -maxheap[0]
        else:
            return 0
