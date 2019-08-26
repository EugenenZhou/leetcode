import time
# 斐波那契数列:
# 实现斐波那契数列

# 青蛙跳台阶：
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

# 矩形覆盖
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
######################################################################
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
######################################################################

s = Solution()
num = 30
st = time.time()
res = s.Fibonacci(num)
ft = time.time()
print(ft - st)

# 递归太慢