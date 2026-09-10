class Solution(object):
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return [u, v]

            parent[pu] = pv