class Solution(object):
    def climbStairs(self, n, costs):
        a=costs[0] + 1
        if n==1:
            return a
        b=costs[1] + min(4, a+1)
        if n==2:
            return b
        c=costs[2] + min(9,b+1, a+4)
        
        for i in range(3,n):
            temp=costs[i]+min(a+9,b+4,c+1)
            a=b
            b=c
            c=temp
        return c