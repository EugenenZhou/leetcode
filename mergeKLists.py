# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def mergeKLists(lists):
    # 暴力法
    head = ListNode(0)
    dummy = head
    res = []
    for i in lists:
        while i:
            res.append(i.val)
            i=i.next
    res.sort()
    for i in res:
        dummy.next = ListNode(i)
        dummy = dummy.next
    return head.next
    #
    # head = ListNode(0)
    # dummy = head
    #



    pass
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
a1 =ToListNode([1,4,5])
a2 =ToListNode([1,3,4])
a3 =ToListNode([2,6])
lists = [a1,a2,a3]
result = mergeKLists(lists)
print(result)
