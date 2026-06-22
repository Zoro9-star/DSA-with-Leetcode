class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        elif n > 2:
            if n % 2 == 0 and n % 3 == 0 and n%5 == 0:
                return True
        else:
            return False
obj = Solution()
print(obj.isUgly(14))