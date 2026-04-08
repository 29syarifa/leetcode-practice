# Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

# Time: O(n)
# Space: O(n)

# use a set to track numbers weve seen
# if we see the same number again >> its a duplicate

# simple and fast no need to compare every pair ya