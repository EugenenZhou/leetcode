# -*- coding:utf-8 -*-
# 合并两个链表

# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

#
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
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        head = ListNode(0)
        dump = head
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        one = pHead1
        two = pHead2
        while one != None and two != None:
            if one.val < two.val:
                dump.next = ListNode(one.val)
                dump = dump.next
                one = one.next
            else:
                dump.next = ListNode(two.val)
                dump = dump.next
                two = two.next
        if one == None:
            dump.next = two
        else:
            dump.next = one
        return head.next
        # write code here

######################################################################








