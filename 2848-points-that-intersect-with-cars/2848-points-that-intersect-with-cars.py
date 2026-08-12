class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        x=set()
        for i in nums:
            for j in range(i[0],i[1]+1):
                if j not in x:
                    x.add(j)
        return len(list(x))