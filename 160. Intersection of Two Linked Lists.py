class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(5)
l4 = ListNode(6)
l5 = ListNode(0)
l6 = ListNode(-4)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l6
l5.next = l6


def getIntersectionNode(headA, headB):
    l1 = 0
    l2 = 0
    ans = []
    saveh1, saveh2 = headA, headB
    while headA:
        l1+=1
        headA = headA.next
    while headB:
        l2+=1
        headB = headB.next
    if l1<=l2:
        while saveh1:
            ans.append(saveh1)
            saveh1 = saveh1.next
        while saveh2:
            if saveh2 in ans:
                return saveh2
            saveh2 = saveh2.next
    else:
        while saveh2:
            ans.append(saveh2)
            saveh2 = saveh2.next
        while saveh1:
            if saveh1 in ans:
                return ans
            saveh1 = saveh1.next


print(getIntersectionNode(l1,l5))