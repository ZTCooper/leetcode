#    Definition for singly - linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        r = result = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                result.next = ListNode(l2.val)
                l2 = l2.next
            result = result.next
            if l2 and (l1 == None):
                while l2:
                    result.next = ListNode(l2.val)
                    l2 = l2.next
                    result = result.next
            elif l1 and (l2 == None):
                while l1:
                    result.next = ListNode(l1.val)
                    l1 = l1.next
                    result = result.next
        return r.next
