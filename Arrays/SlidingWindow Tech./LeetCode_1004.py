# QUES NO 1004 - Max Consecutive Ones-iii

# Problem Statement:

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.



class Solution:
    def longestOnes(self, nums, k: int) -> int:
        seen = {}
        res = 0
        low=0
        maxCount=0
        for high in range(len(nums)):
            if nums[high] in seen:
                seen[nums[high]]+=1
            else:
                seen[nums[high]]=1
            maxCount=max(maxCount,seen[1] if 1 in seen else 0)

            while (high-low+1) - maxCount>k:
                seen[nums[low]]-=1
                low+=1
            res = max(res,high-low+1)
        return res