# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if(not head or not head.next):
            return True
        
        slow = head
        fast = head
        # First Find the  Middle element 
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        '''
        after finding the middile element
        -> first list
        -> second list
        '''

        # Reverse the second list
        curr = slow
        prev = None

        while(curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # Compare the both first and seconds lists halfs

        first = head
        second = prev

        while(second):
            if(first.val != second.val):
                return False
            first = first.next
            second = second.next
        return True