class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(7)
l2 = ListNode(7)
l3 = ListNode(7)
l4 = ListNode(7)

l1.next = l2
l2.next = l3
l3.next = l4


def removeElements(head, val):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    while val in ans:
        ans.remove(val)
    cur = lol = ListNode(0)
    for i in ans:
        cur.next = ListNode(i)
        cur = cur.next
    return lol.next

print(removeElements(head = l1, val = 7))

# Input: head = [7,7,7,7], val = 7
# Output: []