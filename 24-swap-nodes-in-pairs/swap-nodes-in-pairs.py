# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(not head or not head.next):
            return head
            
        # Set second node to temp
        temp = head.next
        head.next = self.swapPairs(temp.next) # Recurisevely swap the list
        temp.next = head 

        return temp 