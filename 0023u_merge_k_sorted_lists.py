# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        l = len(lists)
        range(0, l - ,)
        pass

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:              
        head = ListNode(0)
        cur = head
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return head.next

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
