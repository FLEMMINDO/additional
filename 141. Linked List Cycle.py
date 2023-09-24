class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)

l1.next = l2
l2.next = l3
l3.next = l4

def hasCycle(head):
    ans = []
    while head:
        if head in ans:
            return True
        ans.append(head)
        head = head.next
    return False



print(hasCycle(l1))
