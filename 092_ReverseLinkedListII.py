# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from email import header


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        # We want to store three parts
        # Before sub-list <head -> left>
        # Sub-list        < left -> right>
        # After sub-list  < right -> end>

        if left == right:
            return head

        curr = head
        prev = None
        i = 0

        # Iterate through (left-1) nodes to arrive at (left)
        while curr is not None and i < left - 1:
            prev = curr
            curr = curr.next
            i += 1

        # Store the node before the sublist to link again later
        last_before_sublist = prev
        # After reversing sub-list, curr becomes the last node of the sublist
        last_sublist = curr
        # 
        next = None
        i = 0

        # Reverse sub-list between left and right
        while curr is not None and i < right - left + 1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        
        # Connect to first part
        if last_before_sublist is not None:
            # (prev) is the first node of the sub-list after reversal
            last_before_sublist.next = prev
        # left == 1, first node is being changed
        else:
            head = prev

        # Connect last part
        last_sublist.next = curr
        return head