class Solution(object):

  def findJudge(self, n, trust):
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """
    scores = [0] * (n + 1)

    for u, v in trust:
      scores[u] -= 1  # u trusts someone (out-degree)
      scores[v] += 1  # v is trusted (in-degree)

    for i in range(1, n + 1):
      if scores[i] == n - 1:
        return i

    return -1