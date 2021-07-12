# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: [ListNode]) -> ListNode:
    # 老实人：多指针，遍历链表数组，每轮找一个当前一个最小值，时间应该是O(N*M)
    ll = len(lists)
    tl = 0
    for i in range(ll):
        node = lists[i]
        while(node != None):
            tl += 1
            node = node.next
    re = ListNode()
    head = re
    for i in range(tl):
        e = 10001
        temp = -1
        for j in range(ll):
            node = lists[j]
            if (node == None):
                continue
            if node.val < e:
                e = node.val
                temp = j
        re.next = lists[temp]
        re = re.next
        lists[temp] = lists[temp].next
    return head.next


def mergeKLists2(lists: [ListNode]) -> ListNode:
    # 鸡贼法：用list重装，排序，再填充到链表中
    ll = len(lists)
    l = []
    for i in range(ll):
        node = lists[i]
        while(node != None):
            l.append(node.val)
            node = node.next
    l.sort()
    re = ListNode()
    head = re
    for i in range(len(l)):
        re.next = ListNode(l[i])
        re = re.next
    return head.next
