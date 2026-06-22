# QUES NO. 844 - Backspace String Compare

#Problem Description:
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".


# Simply we have to compare the string after deleting the # and it's previous elements..



class Solution:
    def SUbarray(self,s,t):
        i = len(s)-1
        j = len(t)-1
        s_count = 0
        t_count = 0

        while i >= 0 or j>= 0:
            while i>= 0:
                if s[i] == "#":
                    s_count += 1
                    i -= 1
                elif s_count > 0:
                    s_count -= 1
                    i -=1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    t_count += 1
                    j -= 1
                elif t_count > 0:
                    t_count -= 1
                    j -= 1
                else:
                    break
            if i>=0 and j>=0:
                if s[i] != t[j]:
                    return False
            elif i>= 0 or j>=0:
                return False
            i-= 1
            j-=1
        return True
    
obj = Solution()
print(obj.SUbarray(s = "a#c", t = "b"))