def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if t == "": return ""

    countT, window = {}, {}

    for c in t:
        countT[c] = 1 + countT.get(c)
    have, need = 0, len(countT)