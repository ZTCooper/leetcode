# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return

        r = head
        while head.next:
            # delete the current ListNode
            if head.val == val:
                n = head.next
                head.val = n.val
                head.next = n.next
                n.next = None
            # record the former ListNode
            else:
                f = head
                head = head.next
        # check the last ListNode
        if head.val == val:
            try:
                head = f
                head.next = None
            # f is unassighed which means all the former Node has been deleted
            # so return
            except UnboundLocalError:
                return
        return r
