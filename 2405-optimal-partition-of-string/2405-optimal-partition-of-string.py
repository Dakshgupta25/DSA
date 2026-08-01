class Solution(object):
    def partitionString(self, s):
        
        parts = 1
        chars = ""
        for c in s:
            if c in chars:
                parts += 1
                chars = c
            else:
                chars += c
        return parts