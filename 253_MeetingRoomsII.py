def minMeetingRooms(intervals):

    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res



appointments = [[1,4], [2,5], [7,9]]
print(minMeetingRooms(appointments))