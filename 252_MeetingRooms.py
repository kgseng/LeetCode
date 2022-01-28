def can_attend_all_appointments(intervals):

  intervals.sort()

  for i in range(1,len(intervals)):
    # If the start time is less than the previous appt's end time, then we cannot attend.
    if intervals[i][0] < intervals[i-1][1]:
      return False 

  return True


appointments = [[1,4], [2,5], [7,9]]
print(can_attend_all_appointments(appointments))