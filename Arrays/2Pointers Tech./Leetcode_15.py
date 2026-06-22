# QUES NO. 15 - 3Sum

#Problem Description:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def ThreeSum(self,nums):                                                         #Passing a parameter as the nums array
        nums.sort()                                                                  #sorting the array
        i = 0                                                                        # assigning i as 0 which means i is the first index of the array
        
        res = []                                                                     # taking a list as res

        for i in range(len(nums)):                                                   # First loop - i will run from 0 - length of the array

            if i > 0 and nums[i] == nums[i - 1]:                                     #First condition - stmt will run until both of the condition (i > 0) and  and i_th elemnt and i-1_th elemenet are same which means repeating or duplicate value
               continue                                                              # when the first condition will true which means the repeating value will appear in this step it will be skipped
            left = i+1                                                               # assigning left as i+1 such as i is already there at first index
            right = len(nums)-1                                                      # assigning right as len(nums)-1 as indext starts from 0 in python

            while left <right :                                                      # Second condition - 1 < 5 (as right = len(nums)-1)
                if nums[i]+nums[left]+nums[right] == 0:                              # in this condition it is being checked that the sum of the values of index i , left and right = 0 
                    res.append([nums[i],nums[left],nums[right]])                     # if the sum is 0 then the three values will append to the res list.
                    left +=1                                                         #then the left pointer will increase by 1
                    right -=1                                                        # also the right will decreased by 1

                    while left < right and nums[left] == nums[left-1]:               # after the if-stmt execution this stmt checks that left has to be smaller than right and left index value is same as the left-1 index value
                        left += 1                                                    # if the above two condition satisfies then left is increased by 1
                elif nums[i]+nums[left]+nums[right] > 0:                             # if the sum > 0 , this condition basically reduced the right
                    right -= 1
                else:
                    left += 1
        return res
obj = Solution()
print(obj.ThreeSum([-1,0,1,2,-1,-4]))


        
