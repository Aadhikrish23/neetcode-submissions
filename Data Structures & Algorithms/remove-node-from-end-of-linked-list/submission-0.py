# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalnode = 0
        curr=head
        while curr:
            curr=curr.next
            totalnode+=1
        target = totalnode-n+1

        if target ==1:
            return head.next
        
        currpos=1
        curr=head
        while currpos<target-1:
            curr=curr.next
            currpos+=1
        if curr.next:
            curr.next=curr.next.next
        
        return head