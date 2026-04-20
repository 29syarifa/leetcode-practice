# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length


# notes:
# sliding window (var size)

# goal:
# find the longest substring without repeating characters

# use a set to track characters inside current window

# pointers:
# left  >> start of window
# right  >> end of window

# step by step:
# 1. expand window by moving right
# 2. if character not in set:
#    - add it
#    - update max_length
# 3. if character already exists:
#    - shrink window from left
#    - remove characters until duplicate gone
# 4. continue expanding

# example:
# s = abcabcbb

# window grows:
# "a" >> "ab" >> "abc"
# then duplicate a found

# shrink:
# remove a from left
# window becomes bc
# continue...

# key idea:
# maintain a window with unique characters only

# why while?
# because there might be multiple duplicates to remove

# important:
# each character is added and removed at most once
# so total operations = O(n)

# complexity:
# time: O(n)
# space: O(n)