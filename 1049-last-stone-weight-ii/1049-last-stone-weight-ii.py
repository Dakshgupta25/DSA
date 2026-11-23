class Solution(object):
    def lastStoneWeightII(self, stones):
        n=len(stones)
        total=sum(stones)
        dp={}

        def solve(ind,cur):
            if ind==n:
                return abs(total- (2*cur))
            if (ind,cur) in dp:
                return dp[(ind,cur)]
            
            take=solve(ind+1,cur+stones[ind])
            nottake=solve(ind+1,cur)
            dp[(ind,cur)]=min(take,nottake)
            return dp[(ind,cur)]
        return solve(0,0)
