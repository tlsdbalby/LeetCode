# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    new = ListNode(0, None)
    head = new
    while True:
        if (l1 == None):
            new.next = l2
            break
        if (l2 == None):
            new.next = l1
            break
        if l1.val > l2.val:
            new.next = ListNode(l2.val, None)
            l2 = l2.next
        else:
            new.next = ListNode(l1.val, None)
            l1 = l1.next
        new = new.next
    return head.next
