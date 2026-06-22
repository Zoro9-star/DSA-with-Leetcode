# QUES NO. 977 - Squares of a sorted Array
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#So we have to square the values in the array and sorted them by their value in increasing order
# The asking time complexity is O(n)
#
# 
# 
# 
#      _______________________________________________

# a = [1,3,5]
# b = [2,4,6]
# i = 0
# j = 0
# c = []
# while i < len(a) and j < len(b):
#     if a[i] < b[j] or a[i] == b[j]:
#         c.append(a[i])
#         i+=1
#     elif a[i]>b[j]:
#         c.append(b[j])
#         j+=1
# while i < len(a):
#     c.append(a[i])
#     i+=1
# while j < len(b):
#     c.append(b[j])
#     j+=1
        
# print(c)

#_______________This is not the answer.It's just a demo that how can we Merge and sort arrays.





class Solution:
    def Sorted(self,arr):
        neg = []
        pos = []
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
        
        if len(neg)==0:
            return [x**2 for x in pos]
        elif len(pos)==0:
            result = [x**2 for x in neg]
            result.reverse()
            return neg
        else:
            
            pos = [x**2 for x in pos]
            neg = [x**2 for x in neg]
            neg.reverse()
        
        i=j=0
        res = []
        while i<len(neg) and j<len(pos):
              if neg[i] <= pos[j]:
               res.append(neg[i])
               i+=1
              else:
                  res.append(pos[j])
                  j+=1
        while i<len(neg):
            res.append(neg[i])
            i+=1
        while j<len(pos):
            res.append(pos[j])
            j+=1
        return res
        
           



obj = Solution()
print(obj.Sorted([-4,-1,0,3,10]))


