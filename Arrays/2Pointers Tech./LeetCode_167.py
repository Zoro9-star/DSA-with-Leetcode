# Q167) Two Sum ii-input Array is Sorted

#Problem Description:Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.



# I have to import List because Python has no inbuilt List but in Leetcode everything is already settled


from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:     #defining 2 parameters , one is numbers which is a array and target which we have to find
        i = 0                                                           # assigning i as 0 which means the starting point if the array
        j = len(numbers)-1                                              # assigning j as 4-1 =3 because length of the array is 4 but the indices will be end on 3
        while i<j:                                                      # first condition - the loop will stop when i == j or i > j because if this condition will not be there then the loop will not end
            if numbers[i]+numbers[j] == target:                         # fir inner loop - 2+7 == 9 (True)
                return i+1,j+1                                          #first inner loop is true that's why it will return the index values+1 because the question is asking as we have to return 1-based index values since python has 0-based index that's why we have to add 1..
            elif numbers[i]+numbers[j] > target:
                j -= 1
            else:
                i+=1
        return []
obj = Solution()
print(obj.twoSum([2,7,11,15],9))