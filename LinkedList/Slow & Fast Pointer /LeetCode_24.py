# Ques No 24 - Swap Nodes in Pairs

# Problem Statement:
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:

# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]


class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

class Solution:
    def swapPairs(self,head):
        curr = head
        while curr and curr.next:
            curr.val , curr.next.val = curr.next.val , curr.val
            curr = curr.next.next
        return head
obj = Solution()
print(obj.swapPairs(n1))

curr1 = n1
while curr1:
    print(curr1.val,end = "->")
    curr1 = curr1.next
