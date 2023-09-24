class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ln1 = ListNode(1)
ln2 = ListNode(2)
ln3 = ListNode(3)
ln4 = ListNode(4)
ln5 = ListNode(5)
ln1.next = ln2
ln2.next = ln3
ln3.next = ln4
ln4.next = ln5


def reverseBetween(head, left, right):
    headlist = []
    while head:
        headlist.append(head.val)
        head = head.next
    headlist[left-1:right] = headlist[left-1:right][::-1]
    cur = lol = ListNode(0)
    for i in headlist:
        cur.next = ListNode(i)
        cur = cur.next
    return lol.next


print(reverseBetween(ln1, 2, 4))
