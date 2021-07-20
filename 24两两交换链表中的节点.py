class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    re = ListNode(-1, head)
    p1 = re
    p2 = head
    while (p2 != None and p2.next != None):
        p1.next = p2.next
        p2.next = p2.next.next
        p1.next.next = p2
        p1 = p2
        p2 = p2.next
    return re.next


n6 = ListNode(6, None)
n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

param = [n1, n2, n3, n4]
re = swapPairs(n1)
while (re != None):
    print(re.val)
    re = re.next
