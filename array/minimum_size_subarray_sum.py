# Problem: Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        window_sum = 0
        min_len = float('inf')
        
        for right in range(len(nums)):
            window_sum += nums[right]
            
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return 0 if min_len == float('inf') else min_len


# notes:
# this is a sliding window problem
# specifically: variable size window

# goal:
# find the smallest subarray length
# such that the sum >= target

# brute force would check all subarrays
# that would take O(n^2)

# instead i use 2 pointers:
# left  >> start of window
# right >>end of window

# window_sum keeps track of the current window total

# step by step idea:
# 1. expand the window by moving right
# 2. keep adding nums[right] into window_sum
# 3. once window_sum >= target:
#    this means current window is valid
# 4. now try to shrink it from the left
#    because we want the minimum length
# 5. while shrinking:
#    - update min_len
#    - subtract nums[left] from window_sum
#    - move left forward
# 6. stop shrinking when window becomes invalid again
# 7. continue expanding with right

# why while and not if?
# because after reaching the target,
# we want to shrink as much as possible
# to find the shortest valid window

# example:
# target = 7
# nums = [2,3,1,2,4,3]

# right = 0 >> sum = 2
# right = 1 >> sum = 5
# right = 2 >> sum = 6
# right = 3 >> sum = 8  >> valid
# window = [2,3,1,2], length = 4
# shrink from left:
# remove 2 >> sum = 6 >> invalid

# continue
# right = 4 >> sum = 10 >> valid
# window = [3,1,2,4], length = 4
# shrink:
# remove 3 >> sum = 7 >> still valid
# window = [1,2,4], length = 3
# shrink:
# remove 1 >> sum = 6 >> invalid

# continue
# right = 5 >> sum = 9 >> valid
# window = [2,4,3], length = 3
# shrink:
# remove 2 >> sum = 7 >> still valid
# window = [4,3], length = 2
# shrink:
# remove 4 >> sum = 3 >> invalid

# final answer=2

# key idea:
# expandto mqke window valid
# shrink to make it as small as possible

# important insight:
# each element is added once and removed once
# so total work is linear

# complexity:
# time: O(n)
# space: O(1)