class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        dic = set()
        res = 0
        l = 0
        r = 0

        while r < n:
            if s[r] not in dic:
                dic.add(s[r])
            else:
                res = max(res, r - l)

                while s[r] in dic:
                    dic.remove(s[l])
                    l += 1

                dic.add(s[r])

            r += 1

        return max(res, r - l)
