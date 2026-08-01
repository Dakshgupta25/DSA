class Solution(object):
    def partitionString(self, s):
        
        seen = set()
        partitions = 1

        for ch in s:
            if ch in seen:
                partitions += 1
                seen.clear()

            seen.add(ch)

        return partitions