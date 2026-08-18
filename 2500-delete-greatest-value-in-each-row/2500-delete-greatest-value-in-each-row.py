class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        for j in range(len(grid[0])):
            maxx=0
            for i in range(len(grid)):
                a=max(grid[i])
                if maxx<a:
                    maxx=a
                grid[i].remove(a)
            res+=maxx
        return res

