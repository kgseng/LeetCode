def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    
    # two pointers
    # output = running longest valid substring where t in s 
    # while t in s:
    # see if the current window is smaller than the local min window
    # we will shift the the left pointer (increment it)
    # if t not in s:
    # we will shift the right pointer (increment it)

    minWindow = s
    l = 0

    for r in range(1, len(s)):
        # increment r if t not in s
        while t in s[l:r]:
            if len(s[l:r]) < len(minWindow):
                minWindow = s[l:r]
        
    return minWindow

s = 'ABC'
t = 'ASFKASKFABDCL'
print(s in t)
    

    # wip