def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    hashS = {}
    hashT = {}
    
    for c in s:
        hashS[c] = 1 + hashS.get(c,0)
    for c in t:
        hashT[c] = 1 + hashT.get(c,0)

    return hashS == hashT

test = 'racecar'
test2 = 'racecar'
print(isAnagram(test, test2))