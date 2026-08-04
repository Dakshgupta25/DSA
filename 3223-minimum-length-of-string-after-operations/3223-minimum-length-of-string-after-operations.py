class Solution(object):
    def minimumLength(self, s):
        a=[2 if (s.count(x))%2==0 else 1  for x in list(set(s))]
        return sum(a)        