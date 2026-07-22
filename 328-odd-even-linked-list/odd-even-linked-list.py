# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head

        arr = []

        # Collect odd-position values
        temp = head
        while temp is not None:
            arr.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next

        # Collect even-position values
        temp = head.next
        while temp is not None:
            arr.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next

        # Write values back to the list
        temp = head
        i = 0
        while temp is not None:
            temp.val = arr[i]
            i += 1
            temp = temp.next

        return head