def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    temp = str(n)
    res = 0
    for c in temp:
        if c == '1':
            res = res + 1
    return res

n = None
m = 1
print(max(n,m))


# WIP