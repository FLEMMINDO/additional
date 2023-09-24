class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

ln1 = ListNode(7)
ln2 = ListNode(5)


ln1.next = ln2

def reverseList(head):
    # list = []
    # while head:
    #     list.append(head.val)
    #     head = head.next
    # list.reverse()
    # cur = lol = ListNode(0)
    # for i in list:
    #     cur.next = ListNode(i)
    #     cur = cur.next
    # return lol.next
    if head is None:
        return head

    current = head
    previous = None

    while current is not None:
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    return previous


print(reverseList(ln1))

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
