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
def isPalindrome(head):
    # if not head:
    #     return False
    # if head.next:
    #     fast=head.next
    #     slow=head
    #     reverse = ListNode(0)
    #     list = reverse
    #     while fast:
    #         if fast.next:
    #             slow = slow.next
    #             fast = fast.next.next if fast.next else fast.next
    #         else:
    #             break
    #     while slow.next:
    #         temp = ListNode(slow.next.val)
    #         temp.next = list
    #         list = temp
    #         slow = slow.next
    #     while list.next:
    #         if list.val == head.val:
    #             list=list.next
    #             head=head.next
    #         else:
    #             return 'false'
    #     return 'true'
    # else:
    #     return 'true'
    result=[]
    list=head
    while list:
        result.append(list.val)
        list = list.next
    return result == result[::-1]
######################################################################
# L1=[]
# L1=ToListNode(L1)
# result = isPalindrome(L1)
######################################################################



######################################################################
def isPalindromeforint(integer):
#转换成字符
    if (integer % 10 == 0 and integer != 0) or integer < 0:
        return False
    si = str(integer)
    i,j = 0,len(si)-1
    while i < j:
        if si[i] != si[j]:
            return False
        else:
            i, j = i+1, j-1
    return True

#反转一半数字法
    # if (integer % 10 == 0 and integer != 0) or integer < 0:
    #     return False
    # x = 0
    # while integer > x:
    #     x = x * 10 + integer % 10
    #     integer = integer // 10
    # return x == integer or x // 10 == integer

######################################################################
integer = 123
result = isPalindromeforint(integer)


