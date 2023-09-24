# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(4)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(3)

l1.next = l2
l2.next = l3
l3.next = l4

def sortList(head):
    tosort = []
    while head:
        tosort.append(head.val)
        head = head.next
    tosort.sort()
    cur = lol = ListNode(0)
    for i in tosort:
        cur.next = ListNode(i)
        cur = cur.next
    return lol.next

print(sortList(l1))

