# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if(head == None or head.next == None):
            return head
        
        
        odd = head
        even = head.next
        even_head = head.next

        while(even != None and even.next != None):
            odd.next = odd.next.next
            # move the odd pointer
            odd = odd.next
            
            even.next = even.next.next
            # move the even pointer
            even = even.next

        # Here this for the last link
        odd.next = even_head
        return head 