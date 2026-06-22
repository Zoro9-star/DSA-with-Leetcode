class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x<0:
            sign = -1
            x = -x
        while x>0:
            digit = x%10
            res = res*10+digit
            x = x//10
        return res*sign
obj = Solution()
print(obj.reverse(-211))