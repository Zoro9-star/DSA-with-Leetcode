# Ques No 143 - Reorder List

# Problem Statement:
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]






class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
n1 = Listnode(1)
n2 = Listnode(2)
n3 = Listnode(3)
n4 = Listnode(4)
n5 = Listnode(5)

n1.next = n2 
n2.next = n3
n3.next = n4
n4.next = n5

class Solution:
    def reorderList(self,head):
        slow , fast = head , head  
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        def reverse(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        first = head
        second = reverse(slow.next)
        slow.next = None

        while second and first:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2
        
obj = Solution()
print(obj.reorderList(n1))


#This part is only for demonstrate...
curr = n1
while curr:
    print(curr.val, end=" → ")
    curr = curr.next