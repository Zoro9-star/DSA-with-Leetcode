# Given an array arr[] of distinct integers and a value sum, find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.

# Examples :

# Input: sum = 2, arr[] = [-2, 0, 1, 3]
# Output:  2
# Explanation: Triplets with sum less than 2 are (-2, 0, 1) and (-2, 0, 3). 

# Input: sum = 12, arr[] = [5, 1, 3, 4, 7]
# Output: 4
# Explanation: Triplets with sum less than 12 are (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4



class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        count = 0
        for i in range(len(arr)-2):
            left = i+1
            right = len(arr)-1
            
            while left<right:
                if arr[i]+arr[left]+arr[right] < sum and arr[i]<arr[left]<arr[right]:
                    count += (right-left)
                    left += 1
                else:
                    right -=1
        return count
obj = Solution()
print(obj.countTriplets(12,[5, 1, 3, 4, 7]))
                    
        