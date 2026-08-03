class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles = sorted(piles, reverse=True)
        n = len(piles)//3
        result = 0
        for i in range(1, 2*n+1, 2):
            result += piles[i]
        return result
        