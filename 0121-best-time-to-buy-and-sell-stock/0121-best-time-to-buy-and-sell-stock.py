class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi=0
        cur=prices[-1]
        for i in prices[::-1]:
            if i>cur:
                cur=i
            elif cur-i>maxi:
                maxi=cur-i
        return maxi
                
