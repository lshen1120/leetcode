#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        node1 = l1
        node2 = l2
        result = result_head = ListNode(0)
        prev = None
        carry = 0
        while node1 and node2:
            s = node1.val + node2.val
            result.val = (carry + s) % 10
            carry = (s + carry) / 10
            prev = result
            result.next = ListNode(0)
            result = result.next
            node1 = node1.next
            node2 = node2.next

        while node1:
            s = node1.val
            result.val = (carry + s) % 10
            carry = (s + carry) / 10
            prev = result
            result.next = ListNode(0)
            result = result.next
            node1 = node1.next

        while node2:
            s = node2.val
            result.val = (carry + s) % 10
            carry = (s + carry) / 10
            prev = result
            result.next = ListNode(0)
            result = result.next
            node2 = node2.next

        if carry > 0:
            result.val = carry
        else:
            prev.next = None
        return result_head
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print Solution().addTwoNumbers(l1, l2)
# result = result_head =ListNode(0)
