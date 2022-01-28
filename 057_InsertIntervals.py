def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """

    res = []
    for i in range(len(intervals)):
        # If new interval has end value smaller than start value of current interval | no overlap
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        # Else if new interval goes after current interval | no overlap
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        # If there is overlap, then merge the intervals - append merged intervals at end.
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            print(newInterval)
    res.append(newInterval)
    return res



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))