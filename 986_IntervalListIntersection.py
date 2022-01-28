def intervalIntersection(firstList, secondList):
    """
    :type firstList: List[List[int]]
    :type secondList: List[List[int]]
    :rtype: List[List[int]]
    """
    i, j = 0, 0
    res = []

    while i < len(firstList) and j < len(secondList):
        f_start, f_end = firstList[i]
        s_start, s_end = secondList[j]

        # Overlap, append the overlap
        if f_start <= s_end and s_start <= f_end:
            res.append([max(f_start, s_start), min(f_end, s_end)])
        # Squeeze overlap
        # Increment i, this interval has been checked
        if f_end <= s_end:
            i += 1
        else:
            j += 1     
    return res

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(firstList, secondList))