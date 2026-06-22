class SOlution:
    def Duplicate(self,nums):
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        print(count)
        for value in count.values():
            if value >= 2:
                return True
            
        return False
            
obj = SOlution()
print(obj.Duplicate([2,14,18,22,22]))