#Platform - Geeks for Geeks

# You are given a string s consisting only lowercase alphabets and an integer k. 
# Your task is to find the length of the longest substring that contains exactly k distinct characters.

# Note : If no such substring exists, return -1. 

# Examples:

# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

class Solution:
    def LongestSubstring(self,s,k):
        low = 0
        high = 0
        res = 0
        seen = {}
        for high in range(len(s)):
            if s[high] in seen:
                seen[s[high]]+=1
            else:
                seen[s[high]]=1
            while len(seen)>k:
                seen[s[low]]-=1
                if seen[s[low]]==0:
                    del seen[s[low]]
                low+=1
            if len(seen)==k:
                res = max(res,high-low+1) 
        return res 
obj = Solution()
print(obj.LongestSubstring("aababc",3))
