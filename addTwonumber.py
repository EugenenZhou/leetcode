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