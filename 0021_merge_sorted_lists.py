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
    print(sol.mergeTwoLists(None, None))
    print(sol.mergeTwoLists(None, ListNode.new(1,2,3)))
    print(sol.mergeTwoLists(ListNode.new(1,2,3), None))
    print(sol.mergeTwoLists(ListNode.new(1,2,4), ListNode.new(1,3,4)))
