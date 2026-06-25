class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
n1 = Listnode(1)
n2 = Listnode(2)
n3 = Listnode(2)
n4 = Listnode(4)
n5 = Listnode(5)

n1.next = n2 
n2.next = n3
n3.next = n4
n4.next = n5

class Solution:
    def deleteDuplicates(self,head):
        if not head:
            return None
        slow , fast = head , head.next
        while fast:
            if slow.val != fast.val:
                slow = slow.next
                fast = fast.next
            else:
                fast = fast.next
                slow.next = fast
        return head
obj = Solution()
print(obj.deleteDuplicates(n1)) 


curr = n1 
while curr:
    print(curr.val,end="->")
    curr = curr.next
