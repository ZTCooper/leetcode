# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        r = head
        while head.next:
            if head.next.val == head.val:
                nxt = head.next
                head.next = head.next.next
                nxt.next = None
            else:
                head = head.next
        return r
