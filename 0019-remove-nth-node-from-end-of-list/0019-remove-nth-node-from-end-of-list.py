# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None
class Solution(object):
    
    def removeNthFromEnd(self, head, n):
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            fast = dummy
            slow = dummy
            for i in range(n):
                fast = fast.next
            while fast.next != None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return dummy.next