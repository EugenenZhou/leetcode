# 链表中倒数第k个结点

# 输入一个链表，输出该链表中倒数第k个结点。

# 快慢指针
# -*- coding:utf-8 -*-
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
    def FindKthToTail(self, head, k):
        if not head:
            return None
        if k == 0:
            return None
        i = 1
        fast = head
        slow = head
        while i < k:
            if fast.next == None:
                return None
            fast = fast.next
            i = i + 1
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        return slow
        # write code here

######################################################################