class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        a=0
        b=0
        i=0
        j=len(piles)-1
        flag=True
        while i<=j:
            if piles[i]<=piles[j]:
                if flag:
                    a+=piles[j]
                else:
                    b+=piles[j]
                flag!=flag
                j-=1
            else:
                if flag:
                    a+=piles[i]
                else:
                    b+=piles[i]
                flag!=flag
                i+=1
        return a>b