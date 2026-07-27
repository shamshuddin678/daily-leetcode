# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        lessHead = ListNode(0)
        greaterHead = ListNode(0)
        less = lessHead
        greater = greaterHead

        # Partition list into less and greater lists
        while head:
          if head.val < x:
            # Append to less list
            less.next = head
            less = less.next
          else:
            # Append to greater list
            greater.next = head
            greater = greater.next
          head = head.next
      
        # Important: break any existing pointers
        greater.next = None
        less.next = greaterHead.next
      
        return lessHead.next