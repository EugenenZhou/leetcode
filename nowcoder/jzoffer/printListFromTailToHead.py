# -*- coding:utf-8 -*-

# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

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
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # if not listNode:
        #     return[]
        # head = ListNode(listNode.val)
        # while listNode.next is not None:
        #     dummy = ListNode(listNode.next.val)
        #     dummy.next = head
        #     head = dummy
        #     listNode = listNode.next
        # return head
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

        # write code here

######################################################################
lists = [67,0,24,58]
lists = ToListNode(lists)
s =Solution()
result = s.printListFromTailToHead(lists)
print(result)







