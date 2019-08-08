# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
        # write code here
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return None

# 一个栈用来入队，一个栈用来出队