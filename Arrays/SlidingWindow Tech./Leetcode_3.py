# Ques No 3 - Longest SUbstring Without Repeating Characters:

# Problem statement-
# Given a string s, find the length of the longest without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.




class solution:
    def lengthOfLongestSubstring(self, s: str):
        low , high , res = 0,0,0
        seen = {}
        for high in range(len(s)):
            if s[high] in seen:
                seen[s[high]]+=1
            else:
                seen[s[high]]=1
            k = high-low+1
            if len(seen) < k:
                seen[s[low]]-=1
                if seen[s[low]]==0:
                    del seen[s[low]]
                low+=1
                k = high-low+1
            res = max(res , high-low+1)
        return res
obj = solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))