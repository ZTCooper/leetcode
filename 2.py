# Definition for singly-linked list.
# class ListNode():
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        carry = 0
        t = result = ListNode(0)  # 指向同一地址，result后移，t指向头
        while l1 and l2:
            result.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            if l2 and (l1 == None):
                l1 = ListNode(0)
            if l1 and (l2 == None):
                l2 = ListNode(0)
            result = result.next
        if carry:
            result.next = ListNode(carry)

        return t.next
