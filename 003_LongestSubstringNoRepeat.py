# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """


    # store local max len of the current substring
    # or store the actual current substring

    # use a hashmap?
    # store the characters in the hashmap + position
    # if the characters are not in the hashmap, add them
    # if the character is in the mashmap, store the size of the hashmap, then set hasmap to start at position character was found

    l, output = 0, 0
    seenBefore = {}

    for r in range(len(s)):
        if s[r] not in seenBefore:
            output = max(output, r-l+1)
        else:
            if seenBefore[s[r]] < l:
                output = max(output, r-l+1)
            else:
                l = seenBefore[s[r]] + 1
        seenBefore[s[r]] = r
    return output

 



s = 'dvdf'
print(lengthOfLongestSubstring(s))