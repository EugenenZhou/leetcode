# 将两个有序链表合并为一个新的有序链表并返回。
# 新链表是通过拼接给定的两个链表的所有节点组成的。

######################################################################
def mergeTwoLists(l1,l2):
    # head = ListNode(0)
    # dummy = head
    # while l1 is not None and l2 is not None:
    #     if l1.val < l2.val:
    #         dummy.next = ListNode(l1.val)
    #         l1 = l1.next
    #         dummy = dummy.next
    #     else:
    #         dummy.next = ListNode(l2.val)
    #         l2 = l2.next
    #         dummy = dummy.next
    # dummy.next = l2 if l2 else l1
    # return head.next
    #递归
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


######################################################################
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ToListNode(l):
    reason = ListNode(0)
    list = reason
    for num in l:
        list.next = ListNode(int(num))
        list = list.next
    return reason.next
######################################################################
L1 = [1,2,4]
L2 = [1,3,4]
L1 = ToListNode(L1)
L2 = ToListNode(L2)
result = mergeTwoLists(L1,L2)
print(result)
