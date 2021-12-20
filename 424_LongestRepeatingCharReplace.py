def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    
    count = {}
    res = 0
    l = 0

    for r in range(len(s)):
        # increment counter of the character in our hashmap
        # if character doesn't exist in hashmap, return 0
        count[s[r]] = 1 + count.get(s[r],0)

        # while window size - maxFreq > k
        # essentially, if we cannot make k replacements to make our window homogenous
        # we need to increment our left pointer and simultaneously decrement the freq of the character the left pointer was looking at
        while (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        # else we will set our output to be max of any legal window size
        res = max(res, r - l + 1)
    return res

s = "AABABBA"
k = 1
print(characterReplacement(s, k))
