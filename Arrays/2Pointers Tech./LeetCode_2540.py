# Ques No 2540- Minimum Common Value

# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. 
# If there is no common integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.



class SOlution:
    def sorting(self,num1,num2):
        i=0
        j=0
        while i<len(num1) and j<len(num2):
            if num1[i] == num2[j]:
                return num1[i]
            elif num1[i]< num2[j]:
                i+=1
            else:
                j+=1

obj = SOlution()
print(obj.sorting([1,2,3],[2,4]))