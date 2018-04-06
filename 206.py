# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        r = None    # 第一个结点断开
        while head:
            t = head.next   # 旧链表指针后移
            head.next = r   # 向前添加结点到新链表
            r = head        # 新链表指针前移
            head = t        # 头指针复位
        return r
