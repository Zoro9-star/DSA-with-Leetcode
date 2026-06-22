# Ques No 4 - Median of Two Sorted Array

# Problem Statement:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i = 0
        j = 0
        arr = []
        while i < len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        while i<len(nums1):
            arr.append(nums1[i])
            i+=1
        while j<len(nums2):
            arr.append(nums2[j])
            j+=1
        if len(arr) % 2 == 0:
            return float(arr[len(arr)//2]+arr[len(arr)//2 - 1])/2
        else:
            return (arr[len(arr)//2])
obj = Solution()
print(obj.findMedianSortedArrays([1,2],[3]))