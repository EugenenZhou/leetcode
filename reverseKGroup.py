# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def reverseKGroup(head,k):
    # 非递归
    if k == 1:
        return head
    dummy = ListNode(0)
    dum = dummy
    while head != None:
        temp = ListNode(0)
        tem = temp
        for i in range(k):
            if head == None:
                dum.next = temp.next
                return dummy.next
            nex = ListNode(head.val)
            tem.next = nex
            tem = tem.next
            head = head.next
        temp = reverse(temp.next)
        dum.next = temp
        for i in range(k):
            dum = dum.next
    return dummy.next
def reverse(temp):
    dummy = ListNode(temp.val)
    while temp.next != None:
        Node = ListNode(temp.next.val)
        Node.next = dummy
        dummy = Node
        temp = temp.next
    return dummy
# 递归
#     cur = head
#     count = 0
#     while cur and count != k:
#         cur = cur.next
#         count += 1
#     if count == k:
#         cur = self.reverseKGroup(cur, k)
#         while count:
#             tmp = head.next
#             head.next = cur
#             cur = head
#             head = tmp
#             count -= 1
#         head = cur
#     return head
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
lists = [1,2]
lists = ToListNode(lists)
k=2
result = reverseKGroup(lists,k)
print(result)