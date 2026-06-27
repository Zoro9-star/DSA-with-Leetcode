# Ques No 152 - Maximum Product Subarray

# Problem Statement:
# Given an integer array nums, find a that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



class Solutionn:
    def maxProduct(self, nums):
        best = nums[0]
        ans = nums[0]
        minimum = nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = nums[i]*best
            v3 = nums[i]*minimum

            best = max(v1,v2,v3)
            minimum = min(v1,v2,v3)

            ans = max(ans , best , minimum)
        return ans
obj = Solutionn()
print(obj.maxProduct([2,-5,-2,-4,3]))