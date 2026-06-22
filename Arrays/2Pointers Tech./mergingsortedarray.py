class solution:
    def sorting(self,num1,num2):
        i = 0
        j = 0
        res = []
        while i<len(num1) and j<len(num2):
            if num1[i] >= num2[j]:
                res.append(num2[j])
                j+=1
            else:
                res.append(num1[i])
                i+=1
        while i<len(num1):
                res.append(num1[i])
                i+=1
        while j<len(num2):
                res.append(num2[j])
                j+=1
        return res
obj = solution()
print(obj.sorting([1,4,6,8],[2,3,5,7]))