# 栈的压入弹出顺序

# 输入两个整数序列，第一个序列表示栈的压入顺序，
# 请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。
# （注意：这两个序列的长度是相等的）

######################################################################
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        temp_stack = []
        i = 0
        while pushV:
            if not temp_stack or popV[i] != temp_stack[-1]:
                temp_stack.append(pushV.pop(0))
            while temp_stack and popV[i] == temp_stack[-1]:
                temp_stack.pop()
                i = i + 1
        if temp_stack:
            return False
        else:
            return True
        # write code here
######################################################################
push = [1,2,3,4,5]
pop = [5,4,3,2,1]
s = Solution()
res = s.IsPopOrder(push,pop)
print(res)




