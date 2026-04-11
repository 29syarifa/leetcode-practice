# Problem: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        
        # prefix (left)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # suffix (right)
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result

# notes:
# i avoid division by using prefix and suffix products

# prefix : product of all elements to the left
# suffix : product of all elements to the right

# step 1:
# fill result with prefix values

# step 2:
# multiply each position with suffix values

# example:
# nums = [1,2,3,4]

# prefix pass:
# result = [1,1,2,6]

# suffix pass:
# result = [24,12,8,6]

# idea:
# result[i] = left_product * right_product

# complexity:
# time: O(n)
# space: O(1)