class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        heap=[]
        for i in range(len(mat)):
            heap.append([sum(mat[i]),i])
        heapq.heapify(heap)
        res=[]
        for i in range(k):
            a=heapq.heappop(heap)
            res.append(a[1])
        return res
