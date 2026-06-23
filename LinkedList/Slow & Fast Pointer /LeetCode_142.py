# Ques No 142 - Linked List Cycle-ii 

# Problem statement:
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

 

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.



class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


#This is code part for Leetcode

class Solution:
    def detectCycle(self,head):
        slow , fast = head , head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
               slow = head 

               while slow != fast:
                   slow = slow.next
                   fast = fast.next
               return slow
        return None
obj = Solution()
print(obj.detectCycle(node1))
