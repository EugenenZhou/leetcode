# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def swapPairs(head):
    # 递归
    # 1 终止条件
    if head == None or head.next == None:
        # 2 返回值
        return head
    # 3 递归过程
    nexts = head.next
    head.next = swapPairs(nexts.next)
    nexts.next = head
    # 2 返回值
    return nexts
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
heads = [1,2,3,4]
heads = ToListNode(heads)
result = swapPairs(heads)
print(result)


