# Here is a given array , You have to find 2 numbers that their sum will be equal to the targeted number
#(Here it is asking to return the numbers not the indexes , so we can sort it)

#The given array is [1,2,5,6,7] and the target is 9

class Solution:
    def findingtarget(self,arr,k): #Here k is target
        i = 0
        j = len(arr)-1   #J is (5-1)= 4
        while i<j:    # 0<4 (True)
            if arr[i]+arr[j] == k:  #first condition , 1+7 = 6(False)
                return arr[i],arr[j]
            elif arr[i]+arr[j] > k:  #second condition 1+7=8>6(True)
                j-=1  #Therefore j will be reduced by 1 , now j = 3
            else:
                i+=1
        return -1


obj = Solution()
print(obj.findingtarget([1, 2, 5, 6, 7],6))