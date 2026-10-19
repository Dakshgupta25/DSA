class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        cur1=cur2=None
        cnt1=cnt2=0
        for i in nums:
            if i==cur1:
                cnt1+=1
            elif i==cur2:
                cnt2+=1
            elif cnt1==0:
                cur1=i
                cnt1=1
            elif cnt2==0:
                cur2=i
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1=cnt2=0
        res=[]

        for i in nums:
            if i==cur1:
                cnt1+=1
            elif i==cur2:
                cnt2+=1
        if cnt1> (len(nums)//3):
            res.append(cur1)
        if cnt2> (len(nums)//3):
            res.append(cur2)
        return res