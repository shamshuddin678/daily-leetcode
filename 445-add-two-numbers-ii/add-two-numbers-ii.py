# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverse(self, head):

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


    def addTwoNumbers(self, l1, l2):

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        carry = 0

        dummy = ListNode(-1)
        cur = dummy

        while l1 or l2 or carry:

            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            cur.next = ListNode(total % 10)

            carry = total // 10

            cur = cur.next

        return self.reverse(dummy.next)