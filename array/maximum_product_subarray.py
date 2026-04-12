# Problem: Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            result = max(result, max_prod)
        
        return result

# notes:
# similar to maximum subarray but with multiplication

# i track both max and min products
# because a negative number can flip them

# if num is negative:
# swap max_prod and min_prod

# then update:
# max_prod = max(current number OR extend previous product)
# min_prod = min(current number OR extend previous product)

# example:
# nums = [2,3,-2,4]

# negative numbers can turn small >> big

# key idea:
# always keep track of both extremes

# complexity:
# time: O(n)
# space: O(1)