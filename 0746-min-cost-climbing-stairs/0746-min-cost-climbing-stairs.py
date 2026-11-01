class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        a=cost[0]
        b=cost[1]
        for i in range(2,len(cost)):
            c=min(a+cost[i],b+cost[i])
            a=b
            b=c
        return(min(a,b))