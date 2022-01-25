def findMaxVacationLength (workArray, pto):
    # Sliding Window
    # T = paid holiday
    # F = can PTO
    # [T, F, T, T, F, F, F, T]

    from collections import defaultdict

    left = 0
    ans = 0
    workDict = defaultdict(int)

    for right in range(len(workArray)):
        workDict[workArray[right]] += 1
        while workDict['F'] > pto:
            workDict[workArray[left]] -= 1
            left += 1
        ans = max(ans, right-left+1)
    return ans

work = ['T', 'F', 'T', 'T', 'F', 'F', 'F', 'T']
pto = 2
print(findMaxVacationLength(work, pto))

# Time O(n) : iterating through array
# Space O(n): creating dictionary of O(n) | alternatively use a variable since there are only two outcomes