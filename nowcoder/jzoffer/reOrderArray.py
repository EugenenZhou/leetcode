# 调整数组顺序使奇数位于偶数前面

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。

######################################################################
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        last = len(array) - 1
        i = 0
        while i <= last:
            if array[i] % 2 == 0:
                array.append(array[i])
            i = i + 1
        i = i - 1
        while i >= 0:
            if array[i] % 2 != 0:
                array[last] = array[i]
                last = last - 1
            i = i - 1
        return array[last + 1::]
        # write code here

######################################################################