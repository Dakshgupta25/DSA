class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        n=len(piles)
        
        res=0
        for i in range(0,n-n//3,2):
            res+=piles[i+1]
        return res