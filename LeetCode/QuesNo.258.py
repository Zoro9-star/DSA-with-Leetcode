class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
           return num
        while num >= 10:
            sum = 0
            temp = num
            while temp > 0:     
                sum += temp % 10
                temp //= 10
            num = sum
        return num
            
obj = Solution()
print(obj.addDigits(99))