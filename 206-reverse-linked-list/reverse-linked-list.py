# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None:
            return head
        temp = head
        a=[]
        while(temp!=None):
            a.append(temp.val)
            temp=temp.next
        a=a[::-1]
        temp=head
        for i in a:
            temp.val=i
            temp=temp.next
        return head


        