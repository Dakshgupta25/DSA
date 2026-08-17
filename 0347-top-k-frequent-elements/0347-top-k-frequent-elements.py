class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        top_k = [item[0] for item in sorted_items[:k]]

        return top_k
