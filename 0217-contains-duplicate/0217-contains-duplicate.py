class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp={}
        for i in nums:
            if i in mp:
                return True
            else:
                mp[i]=1
        return False