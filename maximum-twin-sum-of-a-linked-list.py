# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ls=[]
        curr=head
        while curr:
            ls.append(curr.val)
            curr=curr.next
        st,end=0,len(ls)-1
        ans=0
        while st<end:
            ans=max(ans,ls[st]+ls[end])
            st+=1
            end-=1
        return ans
        