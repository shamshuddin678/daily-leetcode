# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if(not head or left == right):
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        # Here prev pointer moves the before of left pointer
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        
        # Here  onwards reversing starts
        curr = prev.next

        #  Reverse the links
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next