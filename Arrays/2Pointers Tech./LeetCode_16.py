# QUES NO. 16 - 3SUm CLosest

#Problem description - 
# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def ThreeSum(self,nums,target):
        nums.sort()

        max_diff = float('inf')
        res = nums[0]+nums[1]+nums[2]


        for i in range(len(nums)):
            left  = i+1
            right = len(nums)-1
            
            while left < right:
                
                sum = nums[i]+nums[left]+nums[right]
                if sum == target:
                    return sum
                elif sum < target :
                    diff = abs(sum-target)
                    if diff<max_diff:
                        max_diff = min(max_diff,diff)
                        res = sum
                    left+=1
                else:
                    diff = abs(sum-target)
                    if diff < max_diff:
                        max_diff = min(max_diff,diff)
                        res = sum
                    right-=1
        return res
obj = Solution()
print(obj.ThreeSum([-1,2,1,-4],1))