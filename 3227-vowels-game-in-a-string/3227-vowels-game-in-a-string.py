class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels=set("aeiou")

        for ch in s:
            if ch in vowels:
                return True

        return False
