# Ques No 560 - Subarray Sum equals K

# Problem Statement:
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

 

class Solution:
    def SubarraySum(self,nums,k):
        sum = 0
        seen = {0:1}
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            need = sum - k
            if need in seen:
                count += seen[need]
            seen[sum] = seen.get(sum , 0)+1
        return count
obj = Solution()
print(obj.SubarraySum([1,1,1],2))