# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        nxt = slow.next
        slow.next = None    # 前一半，head指头
        slow = nxt          # 后一半，slow指头，fast指尾
        # reverse
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare node with head
        while node:
            if node.val != head.val:
                return False
            else:
                node = node.next
                head = head.next
        return True
