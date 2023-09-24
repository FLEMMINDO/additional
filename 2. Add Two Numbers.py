import collections


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

ln1 = ListNode([2,4,3])
ln2 = ListNode([5,6,4])


ln1.next = ln2


def addTwoNumbers(l1, l2):
    first = [2,4,3]
    second = [5,6,4]
    str1 = ''
    str2 = ''
    # while l1:
    #     first.append(l1.val)
    #     l1 = l1.next
    # while l2:
    #     second.append(l2.val)
    #     l2 = l2.next
    first.reverse()
    second.reverse()
    for i in first:
        str1 += str(i)
    for i in second:
        str2 += str(i)
    ansdg = int(str1)+int(str2)
    del first[:]
    for i in str(ansdg):
        first.append(int(i))
    first.reverse()
    cur = dummy = ListNode(0)
    for e in first:
        cur.next = ListNode(e)
        cur = cur.next
        print(cur.val)
    return dummy.next


print(addTwoNumbers(ln1, ln2))