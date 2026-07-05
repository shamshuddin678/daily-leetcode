# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        '''
        s1 = ""
        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next

        s2 = ""
        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next

        add = int(s1) + int(s2)

        dummy = ListNode(0)
        curr = dummy

        if add == 0:
            return ListNode(0)

        while add:
            curr.next = ListNode(add % 10)
            curr = curr.next
            add //= 10

        return dummy.next  '''


        # Method 2 Dummy node Method
        t1 = l1
        t2 = l2

        dummy = ListNode(-1)
        cur = dummy
        carry = 0

        while t1 != None or t2 != None:

            total = carry

            if t1:
                total += t1.val      #  t1 instead of l1

            if t2:
                total += t2.val      #  t2 instead of l2

            new_node = ListNode(total % 10)

            carry = total // 10      # Integer division

            cur.next = new_node
            cur = cur.next

            if t1:
                t1 = t1.next

            if t2:
                t2 = t2.next

        if carry:
            cur.next = ListNode(carry)   #  ListNode (capital L)

        return dummy.next                     