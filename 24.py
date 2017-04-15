# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head == None:
            return None
        if head.next:
            a = head
            b = head.next
            c = b.next
            b.next = a
            a.next = self.swapPairs(c)
            return b
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
