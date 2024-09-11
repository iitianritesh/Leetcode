# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node and a pointer for the result linked list
        dummy = ListNode(0)
        head = dummy
        carry = 0
        
        # Iterate through both lists until both are exhausted
        while l1 or l2:
            # Get values from the current nodes, or 0 if the node is None
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            s = v1 + v2 + carry
            carry = s // 10
            
            # Create a new node for the sum and attach it to the result list
            head.next = ListNode(s % 10)
            head = head.next
            
            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there is any carry left after the last operation, add a new node
        if carry:
            head.next = ListNode(carry)
        
        # Return the next node of the dummy node, which is the head of the result list
        return dummy.next
