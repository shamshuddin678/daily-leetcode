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

        ''' 
        Brute force solution : 
        arr = []
        # Here this jump for odd index data
        temp = head
        while(temp != None and temp.next != None):
            arr.append(temp.val)
            temp = temp.next.next
        if(temp): # This is for last node data
            arr.append(temp.val)
        
        # Here this is for even index data
        temp = head.next
        while(temp != None and temp.next != None):
            arr.append(temp.val)
            temp = temp.next.next
        if(temp): # This is for last node data 
            arr.append(temp.val)
        i = 0
        temp = head
        while(temp != None):
            temp.val = arr[i]
            i += 1
            temp = temp.next
        return head  '''

        # Optimised solution
        odd = head
        even = head.next
        even_head = head.next
        
        # Here condition is the : if even has reached the end or not . if even has reached the end then odd also reach
        while(even != None and even.next != None):
            #  Here change the links
            odd.next = odd.next.next 
            even.next = even.next.next

            #  pointers moving
            odd = odd.next
            even = even.next
            
            #  Here this is for the last link for odd to even
        odd.next = even_head
        return head        

