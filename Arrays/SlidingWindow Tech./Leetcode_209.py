# QUES NO 209 - MInimum Size SUbarray Sum

#Problem Statement:
# Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


class Solution:
    def minSubArrayLen(self, target: int, nums):
        low = 0
        high = 0
        sum=0
        res = float("inf")
        while high<len(nums):
            sum = sum + nums[high]
            while sum >= target:
                length = high-low+1
                res = min(res,length)
                sum = sum - nums[low]
                low+=1
            high+=1
        return 0 if res == float("inf") else res
    
obj = Solution()
print(obj.minSubArrayLen([2,3,1,2,4,3]))