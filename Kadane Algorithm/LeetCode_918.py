# Ques No 918 - Maximum Sum Circular Array

# Problem Statement:
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.



class Solution:
    def maxSubarraySumCircular(self, nums):
        best = nums[0]
        bestAns = nums[0]
        mini = nums[0]
        minAns = nums[0]

        for i in range(1,len(nums)):
            best = max(best+nums[i],nums[i])
            bestAns = max(bestAns , best)
        for i in range(1,len(nums)):
            mini = min(mini+nums[i],nums[i])
            minAns = min(minAns,mini)
        total = sum(nums)
        if bestAns < 0:
            return bestAns
        return max(bestAns , total-minAns)
        
obj = Solution()
print(obj.maxSubarraySumCircular([1,-2,3,-2]))