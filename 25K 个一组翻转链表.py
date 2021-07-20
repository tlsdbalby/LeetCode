# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    if (k == 1):
        return head
    re = ListNode(0, head)
    p1 = re
    p2 = head
    i = 1
    while (p2 != None):
        if (i != k):
            p2 = p2.next
            i += 1
        else:
            nl = []
            temp = p1.next
            while (temp != p2):
                nl.append(temp)
                temp = temp.next
            p1.next = p2
            nl[0].next = p2.next
            for j in range(len(nl)-1, -1, -1):
                p2.next = nl[j]
                p2 = p2.next
            p1 = p2
            p2 = p2.next
            i = 1
    return re.next


n6 = ListNode(6, None)
n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

re = reverseKGroup(n1, 7)
while (re != None):
    print(re.val)
    re = re.next
