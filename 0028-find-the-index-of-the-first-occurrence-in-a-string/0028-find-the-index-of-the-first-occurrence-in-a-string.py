class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n=len(needle)
        m=len(haystack)
        # Build LPS array
        lps = [0] * n

        length = 0
        i = 1

        while i < n:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # KMP search
        i = 0  # haystack
        j = 0  # needle

        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == n:
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1