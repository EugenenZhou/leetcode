import time

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # 递归
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 1
        # return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        # 循环法
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        x = 1
        y = 1
        while n > 2:
            y = x + y
            x = y - x
            n = n - 1
        return y


s = Solution()
num = 30
st = time.time()
res = s.Fibonacci(num)
ft = time.time()
print(ft - st)

# 递归太慢