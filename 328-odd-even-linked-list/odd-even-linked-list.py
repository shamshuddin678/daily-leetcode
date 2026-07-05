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
        return head            
