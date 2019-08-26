# 二维数组中的查找
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。


# 提示：从右上角开始
######################################################################
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # if target == array[0][0]:
        #     return True
        # if target < array[0][0]:
        #     return False
        # if array[0][0] == array[-1][0] or array[0][0] == array[0][-1]:
        #     return True if target in array else False
        # if target > array[0][0]:
        #     return self.Find(target, array[1::][:]) or self.Find(target, array[:][1::])
        if array == [[]]:
            return False
        i = 0
        while i >= 0:
            if target in array[i]:
                return True
            if array[i][0] > target or array[i][0] == array[-1][0]:
                return False
            i = i + 1

        # write code here
######################################################################

target = 7
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
array2 = [[]]
result = Solution()
re = result.Find(target,array2)



