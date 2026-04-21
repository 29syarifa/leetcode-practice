# Problem: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        prefix_map = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            if (prefix_sum - k) in prefix_map:
                count += prefix_map[prefix_sum - k]
            
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        
        return count


# notes:
# prefix sum + hashmap

# goal:
# count how many subarrays have sum == k

# brute force:
# check all subarrays >> O(n^2)

# optimization:
# use prefix sum

# prefix_sum[i] = sum from index 0 to i

# key idea:
# if:
# current_sum - previous_sum = k
# then:
# subarray between them has sum = k

# rearrange:
# previous_sum = current_sum - k

# so i check:
# "have we seen (prefix_sum - k) before?"

# prefix_map stores:
# prefix_sum >> how many times ive seen it

# why {0:1}?
# to handle subarray starting from index 0

# example:
# nums = [1,1,1], k = 2

# prefix_sum:
# 1 >> 2 >> 3

# when prefix_sum = 2:
# 2 - 2 = 0 >> found in map >> count++

# when prefix_sum = 3:
# 3 - 2 = 1 >> found >> count++

# result = 2

# important:
# we ADD count, not just +1
# because prefix_sum can appear multiple times

# key insight:
# convert subarray problem >> prefix difference problem

# complexity:
# time: O(n)
# space: O(n)