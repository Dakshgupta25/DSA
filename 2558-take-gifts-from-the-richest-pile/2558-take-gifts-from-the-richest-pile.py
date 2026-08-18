class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for i in range(k):
            a = -heapq.heappop(heap)       # get maximum
            a = int(math.sqrt(a))          # floor(sqrt(a))
            heapq.heappush(heap, -a)

        return -sum(heap)
        