# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = follow = head
        for i in range(n):
            tail = tail.next
        if not tail:    # 只有一个结点
            return head.next    # 倒数第n个是第一个结点
        while tail.next:
            tail = tail.next
            follow = follow.next
        follow.next = follow.next.next
        return head
