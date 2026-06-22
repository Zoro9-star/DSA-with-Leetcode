# Ques No 551 - Student Attendance Record:

# Problem Statement-
# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. 
# The record only contains the following three characters:

#     'A': Absent.
#     'L': Late.
#     'P': Present.

# The student is eligible for an attendance award if they meet both of the following criteria:

#     The student was absent ('A') for strictly fewer than 2 days total.
#     The student was never late ('L') for 3 or more consecutive days.

# Return true if the student is eligible for an attendance award, or false otherwise.

 

# Example 1:

# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.



class Solution:
    def checkRecord(self, s: str) -> bool:
        seen ={}
        if s.count('A') >= 2:
            return False
        if 'LLL' in s:
            return False
        return True
obj = Solution()
print(obj.checkRecord("LLLL"))