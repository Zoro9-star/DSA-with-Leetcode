class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        total_sum = n*(n+1)/2
        nums_sum = sum(nums)
        missing_number = int(total_sum - nums_sum) 
        return missing_number
obj = Solution()
print(obj.missingNumber([9,6,4,2,3,5,7,0,1]))