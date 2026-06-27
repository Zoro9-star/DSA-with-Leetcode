# Ques No 53 - Maximum Subarray

# Problem Statement:
# Given an integer array nums, find the with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.



class Solutionn:
    def MaximumSubarray(self, nums):
        best = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            best = max(nums[i],best+nums[i])
            ans = max(best,ans)
        return ans
obj = Solutionn()
print(obj.MaximumSubarray([-2,1,-3,4,-1,2,1,-5,4]))