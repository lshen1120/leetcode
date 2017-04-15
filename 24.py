# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        node = head
        result = head
        prev = None
        while node and node.next:
            left = node
            right = node.next
            bnext = right.next
            # swap
            left.next = bnext
            right.next = left
            node = bnext
            if prev:
                prev.next = right
            prev = left
            if result ==head:
                result=right

        return result
        """
        :type head: ListNode
        :rtype: ListNode
        """
