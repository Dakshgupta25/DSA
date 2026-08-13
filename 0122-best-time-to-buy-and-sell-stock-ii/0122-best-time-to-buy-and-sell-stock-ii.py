class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        cur=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                ans+=max(0,prices[i-1]-cur)
                cur=prices[i]
        ans+=max(0,prices[-1]-cur)
        return ans