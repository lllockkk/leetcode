# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        s = str(self.val)
        p = self.next
        while p:
            s = s + '->' + str(p.val)
            p = p.next
        return s

    @staticmethod
    def new(*vals):
        if not len(vals):
            raise 'error args'
        
        r = reversed(vals)
        node = None
        for i in r:
            node = ListNode(i, node)
        return node


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = None
        for i in range(n-1):
            p = p.next
        
        # 如果刪除的是第一个
        if not p.next:
            return head.next
        p = p.next
        q = head

        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeNthFromEnd(ListNode.new(1), 1))
    print(sol.removeNthFromEnd(ListNode.new(1,2,3,4,5), 2))


# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
