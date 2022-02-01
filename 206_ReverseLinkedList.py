# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from optparse import TitledHelpFormatter


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # None <- 1 <- 2 <- 3 <- 4 <- 5

        prev = None
        curr = head
        next = None

        while curr:
            # 1) Temporarily store the next node
            next = curr.next
            # 2) Reverse the current node
            curr.next = prev
            # 3) Increment previous and current
            prev = curr
            curr = next
        return prev



