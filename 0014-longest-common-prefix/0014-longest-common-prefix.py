class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        # Build Trie
        root = TrieNode()

        for word in strs:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.isEnd = True

        # Find common prefix
        prefix = ""
        node = root

        while len(node.children) == 1 and not node.isEnd:
            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]

        return prefix