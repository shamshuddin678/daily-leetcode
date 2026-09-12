# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []

        temp1 = list1
        temp2 = list2

        while(temp1):
            arr.append(temp1.val)
            temp1 = temp1.next
        while(temp2):
            arr.append(temp2.val)
            temp2 = temp2.next
        arr.sort()

        # both lists are empty
        if(len(arr) == 0):
            return None
        # convert arr back into linked list
        head = ListNode(arr[0])
        temp = head

        for i in range(1,len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return head