'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''
from collections import defaultdict
def longest_substring_with_k_distinct(str,k):
    # Dictionary to store our distinct characters
    counter = defaultdict(int)
    
    left = 0
    ans = 0

    
    for right, c in enumerate(str):
        counter[c] += 1
        # Number of distinct characters > k, increment left pointer
        # Decrement the character the left pointer was at, remove if said count reaches 0
        # Longest substring length, ans, is the max of ans and right-left+1
        # Right pointer is incremented as long as our condition, distinct characters <= k, is valid.
        while len(counter) > k:
            counter[str[left]] -= 1

            if counter[str[left]] == 0:
                del counter[str[left]]
            left += 1
        ans = max(ans, right-left+1)
    return ans

str = "eceba"
k = 2
print(longest_substring_with_k_distinct(str, k))