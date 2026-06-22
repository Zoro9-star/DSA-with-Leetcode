# REMOVE DUPLICATION TECHNIQUE
# SO we have a given array which is sorted so we have to remove duplicate values and return the number of unique values in the array.
#The given array is [1,1,1,2,2,3,3,3]
#We have to return 3 as there are 3 unique values and rearrange the unique values and remove the duplicate values.
#Here duplicate means not deleting , it means place them after rearranging the unique values..


class Solution:
    def RemoveDupli(self,arr):  #passing an array as parameter
        i = 0                   #assigning i as 0 which will be the first index of the array
        unique = 1              # definig a unique variable as 1 which will count the number of unique values (1 because there is always a unique value already)
        cm = 1                  # defining another variable cm =1 which will traverse the array from index 1
        while cm < len(arr):                        # first loop condition- 1<8 (length of the array in this case) (True)
            if arr[cm] == arr[cm-1]:                #Comparing the values - 1 == 1 (True)
                cm += 1                             # First condition is true that's why cm will increase with 1 , cm = 2
            else:
                arr[i+1] = arr[cm]                  # When the first condition will be false , this condition will replace the values 
                unique += 1                         #Whenever the replace condition will be execute , count will be increased by 1
                i += 1                              # Also i will increase by 1 as the condtions are true
                cm += 1                             # Also cm will increase(in every case)
        return unique
abj = Solution()
print(abj.RemoveDupli([0,0,1,1,1,2,2,3,3,4]))