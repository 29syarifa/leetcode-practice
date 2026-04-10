# Problem: two sum
# Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[num] = i

# notes:
# using hashmap to store numbers weve seen
# for each number we check wht we need to reach the target
# if the needed number already exists so we found the answer

# ex:
# nums = [2,7,11,15] target = 9
# 2 need 7
# 7 found 2 before >> return [0,1]

# i solve it in one pass instead of checking every pair

# so complexity:
# time: O(n)
# space: O(n)