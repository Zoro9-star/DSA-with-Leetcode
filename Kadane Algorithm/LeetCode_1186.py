# Ques No 1186 - Maximum Subarray Sum with One Deletion
    
# Problem Statement:
# Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

# Note that the subarray needs to be non-empty after deleting one element.

 

# Example 1:

# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

# Example 2:

# Input: arr = [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.




class Solution:
    def MaximumSum(self,arr):
        no_delete = arr[0]
        one_delete = arr[0]
        ans = arr[0]

        for i in range(1,len(arr)):
            one_delete = max(no_delete,one_delete+arr[i])
            no_delete = max(arr[i],no_delete+arr[i])

            ans = max(ans , no_delete , one_delete)
        return ans
obj = Solution()
print(obj.MaximumSum([1,-2,0,3]))