# 包含min的栈

# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
##### 时间复杂度应为O（1）。####


######################################################################
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        self.stack.append(node)
        if not self.minstack:
            self.minstack.append(node)
        elif node < self.minstack[0]:
            self.minstack[0] = node
        # write code here
    def pop(self):
        if not self.stack:
            return None
        if len(self.stack) == 1:
            self.minstack.pop()
            return self.stack.pop()
        if self.stack[-1] > self.minstack:
            return self.stack.pop()
        else:
            self.minstack[0] = self.stack[0]
            for i in range(len(self.stack)-1):
                if self.stack[i] < self.minstack[0]:
                    self.minstack[0] = self.stack[i]
            return self.stack.pop()
        # write code here
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
        # write code here
    def min(self):
        if not self.stack:
            return None
        return self.minstack[0]
        # write code here

######################################################################