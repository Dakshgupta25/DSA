class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        res=0
        i=0
        while i<len(costs) and costs[i]<=coins:
            coins-=costs[i]
            res+=1
            i+=1
        return res            