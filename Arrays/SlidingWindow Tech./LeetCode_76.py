# QUES N0 76 - Minimum Window Substring

# Problem Statement-
# Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.




class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen={}
        for i in t:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        window={}
        have = 0
        low=0
        need = len(seen)
        resL, resR = 0,0
        res = float("inf")
        for high in range(len(s)):
            if s[high] in window:
                window[s[high]]+=1
            else:
                window[s[high]]=1
            if s[high] in seen and window[s[high]]==seen[s[high]]:
                have+=1

            while have == need:
                if high-low+1 < res:
                    res = high-low+1
                    resL , resR = low , high
                window[s[low]] -= 1
                if s[low] in seen and window[s[low]] < seen[s[low]]:

                    have -= 1 
                low += 1
        
        return "" if res == float("inf") else s[resL:resR+1]

obj=Solution()
print(obj.minWindow("ADOBECODEBANC","ABC"))