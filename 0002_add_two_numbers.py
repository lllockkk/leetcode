class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        s = str(self.val)
        node = self.next
        while node:
            s = str(node.val) + s
            node = node.next
        return s

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(None)
        node = result
        carry = 0
        while l1 or l2 or carry:
            val = self.add(l1, l2) + carry
            val, carry = self.carry(val)
            node.next = ListNode(val)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return result.next

    
    def add(self, l1, l2):
        return (l1.val if l1 else 0) + (l2.val if l2 else 0)

    def carry(self, num):
        if num >= 10:
            return (num-10, 1)
        else:
            return (num, 0)


def toListNode(val):
    result = ListNode(None)
    node = result
    for i in val:
        node.next = ListNode(i)
        node = node.next
    return result.next

if __name__ == "__main__":
    l1 = toListNode( (8,6,3,7,9,4) )
    l2 = toListNode( (4,7,5,8) )
    print(l1, '+', l2, '=', Solution().addTwoNumbers(l1, l2))
