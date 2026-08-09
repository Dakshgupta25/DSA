class Solution(object):
    def pivotIndex(self, nums):
        px=[0]
        sx=[]
        s=sum(nums)
        for i in nums:
            px.append(px[-1]+i)
            s-=i
            sx.append(s)
        for i in range(len(nums)):
            if px[i]==sx[i]:
                return i
        return -1