class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l5 = ListNode(3)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

def deleteDuplicates(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    answer = []
    [answer.append(i) for i in ans if i not in answer]
    cur = lol = ListNode(0)
    for i in answer:
        cur.next = ListNode(i)
        cur = cur.next
    return lol.next

print(deleteDuplicates(l1))

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]