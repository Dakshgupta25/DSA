class Solution(object):
    def minimumLength(self, s):
        freq = [0] * 26
        n = len(s)

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1

            if freq[idx] == 3:
                freq[idx] -= 2
                n -= 2

        return n