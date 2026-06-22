# QUES NO 18 - 4Sum

# Problem Statement:
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]



class Solution:
    def fourSum(self, nums, target: int):
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                low , high = j+1,n-1
                while low < high:
                    sum = nums[i]+nums[j]+nums[low]+nums[high]
                    if sum == target:
                        res.append([nums[i],nums[j],nums[low],nums[high]])
                        low+=1
                        high-=1

                        while low<high and nums[low]==nums[low-1]:
                            low+=1
                        while low<high and nums[high]==nums[high+1]:
                            high-=1
                    elif sum<target:
                        low+=1
                    else:
                        high-=1
        return res
obj = Solution()
print(obj.fourSum([1,0,-1,0,-2,2], target = 0))