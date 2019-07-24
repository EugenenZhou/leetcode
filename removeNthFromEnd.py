# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
# 在真实的面试中遇到过这道题？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
######################################################################
def removeNthFromEnd(head, n):
    # 两次遍历
    # dummy =ListNode(0) #哑结点,防止异常情况
    # dummy.next = head
    # length = 0
    # t = head
    # while t.next is not None:
    #     length = length +1
    #     t = t.next
    # n = length - n
    # find_length = 0
    # t = dummy
    # while find_length <= n:
    #     find_length = find_length + 1
    #     t = t.next
    # t.next = t.next.next
    # return dummy.next
    # 单次遍历
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    for i in range(n):
        first = first.next
    while first.next is not None:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next
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
head = [1,2,3,4,5]
n = 2
ll = ToListNode(head)
print(ll)
result = removeNthFromEnd(ll,n)
print(result)
