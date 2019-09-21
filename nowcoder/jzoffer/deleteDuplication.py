# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    def deleteDuplication(self, pHead):
        h = ListNode(99999)
        h.next = pHead
        slow = h
        fast = slow.next
        while fast and fast.next:
            if fast.val != fast.next.val:
                slow.next = fast
                slow = slow.next
                fast = fast.next
            else:
                p = fast.next
                while p and fast.val == p.val:
                    p = p.next
                fast = p
        slow.next = fast
        return h.next
        # write code here
######################################################################
lists = [1,2,3,4,4,5,5,6]
lists = ToListNode(lists)
s =Solution()
result = s.deleteDuplication(lists)
print(result)