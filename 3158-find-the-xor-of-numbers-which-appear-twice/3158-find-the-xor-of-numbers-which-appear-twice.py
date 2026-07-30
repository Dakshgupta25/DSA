class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        xor=0
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                xor^=i
        return xor