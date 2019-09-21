# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        pointx = 0
        pointy = 1
        length = len(array)
        while pointx < pointy:
            if array[pointx] + array[pointy] == tsum:
                break
            elif array[pointx] + array[pointy] < tsum:
                if pointy < length - 1:
                    pointy += 1
                else:
                    pointx += 1
            elif array[pointx] + array[pointy] > tsum:
                pointx += 1
                pointy -= 1
        return [array[pointx], array[pointy]]

        # write code here



if __name__ == '__main__':
    s = Solution()
    r = s.FindNumbersWithSum([1,2,4,7,11,15],15)
    print(r)