# QUES NO 424 - Longest Repeating Character Replacement

# Problem Statement:

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen ={}
        low=0
        res =0
        maxCount=0
        for high in range(len(s)):
            if s[high] in seen:
                seen[s[high]]+=1
            else:
                seen[s[high]]=1
            maxCount=max(maxCount,seen[s[high]])
            while (high-low+1) - maxCount > k:
                seen[s[low]]-=1
                low+=1
            res = max(res,high-low+1)
        return res
