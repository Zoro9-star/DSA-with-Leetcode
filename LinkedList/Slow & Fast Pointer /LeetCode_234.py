# Ques No 234 - Palindrome Linked List

# Problem statement:
# Given the head of a singly linked list, return true if it is a or false otherwise.

# Example 1:

# Input: head = [1,2,2,1]
# Output: true



class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
n1 = Listnode(1)
n2 = Listnode(2)
n3 = Listnode(3)
n4 = Listnode(2)
n5 = Listnode(1)
n1.next = n2 
n2.next = n3
n3.next = n4
n4.next = n5

class Solution:
    def Palindrome(self,head):
        slow , fast = head , head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        def reverse(head):
            prev = None
            curr = head 
            while curr:
                next = curr.next
                curr.next=prev
                prev = curr
                curr = next
            return prev
        second = reverse(slow)

        first = head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
obj = Solution()
print(obj.Palindrome(n1))