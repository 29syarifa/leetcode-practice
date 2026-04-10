# Problem: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# notes:
# this is kadaness algorithm

# at each step:
# we decide >> start fresh or continue previous subarray

# current_sum =max(current number current_sum + number)

# if previous sum is dragging us down >> drop it
# if its helping >> keep it

# example:
# [-2,1,-3,4,-1,2,1,-5,4]

# i reset when sum becomes worse than starting fresh

# goal:
# always track the best sum weve seen so far

# complexity:
# time: O(n)
# space: O(1)