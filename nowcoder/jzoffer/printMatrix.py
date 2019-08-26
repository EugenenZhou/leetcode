# 顺时针打印矩阵

# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

######################################################################
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        i = 0
        j = -1
        l = 0
        circle = 1
        res = []
        set_i = [0, 1, 0, -1]
        set_j = [1, 0, -1, 0]
        row, column = len(matrix), len(matrix[0])
        total_number = row * column
        row = row - 1
        se = 0
        while total_number > 0:
            setting = se % 4
            if circle % 2 == 1:
                while l < column:
                    i = i + set_i[setting]
                    j = j + set_j[setting]
                    res.append(matrix[i][j])
                    l = l + 1
                    total_number = total_number - 1
                column = column - 1
            else:
                while l < row:
                    i = i + set_i[setting]
                    j = j + set_j[setting]
                    res.append(matrix[i][j])
                    l = l + 1
                    total_number = total_number - 1
                row = row - 1
            circle = circle + 1
            se = se + 1
            l = 0
        return res
        # write code here

######################################################################






