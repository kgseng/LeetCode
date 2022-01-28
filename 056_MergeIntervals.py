# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
#  and return an array of the non-overlapping intervals that cover all the intervals in the input  
#   https://leetcode.com/problems/merge-intervals/discuss/1036776/Simple-Sorting-Python-Solution-O(N-log-N)-time
def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals = sorted(intervals)
    ans = []

    start = intervals[0][0]
    end = intervals[0][1]
    
    for i in intervals:
        if i[0] > end:
            ans.append([start, end])
            start, end = i[0], i[1]
        else:
            end = max(end, i[1])
    ans.append([start, end])
    return ans
 
intervals = [[1,3],[2,6],[8,10],[15,18]]
# [[1,6],[8,10],[15,18]]

print(merge(intervals))