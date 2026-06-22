# QUES - Length of Last Word

# Problem statement-
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.


class Solution:
    def lengthofLastword(self,s):
        lst = list(s.split())
        n = len(lst)-1
        return len(lst[n])
obj = Solution()
print(obj.lengthofLastword("   fly me   to   the moon  "))