# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Here we use the dummy node approach
        temp = ListNode(0)
        temp.next = head
        prev = temp
        curr = head
        while(curr):
            if(curr.val == val): # Here check the curr pointer val == val 
                prev.next = curr.next # Here changes the links prev.next -> curr.next
                curr = curr.next  # here curr moves to next node after sets the link after     
            else:
                prev = curr
                curr = curr.next
        return temp.next           