# -*- coding:utf-8 -*-
# 反转链表

# 输入一个链表，反转链表后，输出新链表的表头。

# 递归法
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
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        newhead = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return newhead

        # write code here

######################################################################








