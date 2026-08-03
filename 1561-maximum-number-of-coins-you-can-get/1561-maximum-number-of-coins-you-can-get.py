class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n=len(piles)
        
        res=0
        for i in range(n//3,n,2):
            res+=piles[i]
        return res