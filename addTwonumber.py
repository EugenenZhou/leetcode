# 给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
# 并且它们的每个节点只能存储一位数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next = None

def ToListNode(l):
    reason=ListNode(0)
    list=reason
    for num in l:
        list.next=ListNode(int(num))
        list=list.next
    return reason.next
######################################################################
def addTwonmuber(l1,l2):
    set=0
    reason=ListNode(0)
    list=reason
    while l1 or l2:
        s1=l1.val if l1 else 0
        s2=l2.val if l2 else 0
        sum = s1 + s2 + set
        set = sum//10
        list.next=ListNode(sum%10)
        list=list.next
        l1=l1.next if l1!= None else None
        l2=l2.next if l2!= None else None
    if set == 1:# easy to forget
        list.next=ListNode(1)
    return reason.next
######################################################################

l1=[0,3,4]
l2=[2,4,5]
L1=ToListNode(l1)
L2=ToListNode(l2)
reason=addTwonmuber(L1,L2)