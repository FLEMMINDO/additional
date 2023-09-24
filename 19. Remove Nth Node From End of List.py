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

# def removeNthFromEnd(head, n):
#     savehead = head
#     lol = head
#     length = 0
#     while head:
#         head = head.next
#         length+=1
#     tmp = ListNode(0)
#     if length == n:
#         return lol
#     while savehead:
#         if n == length-1:
#             tmp = savehead
#         if n == length:
#             tmp.next = savehead.next
#             return lol
#         savehead = savehead.next
#         length-=1
#
# print(removeNthFromEnd(ln1, 4))

def removeNthFromEnd(head, n):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    l.pop(-n)
    ln = cur = ListNode(0)
    for i in l:
        ln.next = ListNode(i)
        ln = ln.next
    return cur.next

print(removeNthFromEnd(ln1, 2))