# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None or k==0:
            return head
        temp=head
        n=1
        while temp.next:
            n+=1
            temp=temp.next
        k=k%n
        if k==0:
            return head
        temp2=head
        for i in range(n-k-1):
            temp2=temp2.next
        x=temp2.next
        temp2.next=None
        temp.next=head
        return x


