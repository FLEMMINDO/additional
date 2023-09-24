class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

ln1 = ListNode([7])
ln2 = ListNode([5])


def mergeTwoLists(list1, list2):
    ans = []
    while list1:
        ans.append(list1.val)
        list1 = list1.next
    while list2:
        ans.append(list2.val)
        list2 = list2.next
    ans.sort()
    cur = lol = ListNode(0)
    for i in ans:
        cur.next = ListNode(i)
        cur = cur.next
    return lol.next

print(mergeTwoLists(ln1,ln2))