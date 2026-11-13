class Solution(object):
    def subsets(self, nums):
        n=len(nums)
        res=[]

        def fun(i,cur):
            if i==n:
                res.append(cur[:])
                return

            cur.append(nums[i])
            fun(i+1,cur)
            cur.pop()
            fun(i+1,cur)
            return
        fun(0,[])
        return res