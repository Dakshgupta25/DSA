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
        
        root=TrieNode()
        for word in strs:
            node=root
            for ch in word:
                if ch not in node.children:
                    node.children[ch]=TrieNode()
                node=node.children[ch]
            node.isEnd=True

        prefix=""

        while len(root.children)==1 and root.isEnd==False:
            ch=list(root.children)[0]
            prefix+= ch
            root=root.children[ch]
        return prefix