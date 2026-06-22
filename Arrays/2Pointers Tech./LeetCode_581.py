# Ques No 581 - SHortest Unsorted Continuous Subarray

# Problem Statement:

# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, 
# then the whole array will be sorted in non-decreasing order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.



class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        left = 0
        right = len(sorted_nums)-1

        while left<len(sorted_nums) and nums[left]==sorted_nums[left]:
            left+=1
        while right>left and nums[right]==sorted_nums[right]:
            right-=1
        
        return right-left+1 if left<len(nums) else 0