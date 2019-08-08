# 把一个数组最开始的若干个元素搬到数组的末尾，
# 我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，
# 输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，
# 该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # 暴力法
        # for i in range(len(rotateArray)):
        # if rotateArray[i] > rotateArray[i+1]:
        # return rotateArray[i+1]
        # 双指针二分查找
        left = 0
        right = len(rotateArray) - 1
        while left + 1 < right:
            mid = int((left + right) / 2)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return min(rotateArray[left], rotateArray[right])

        # write code here

s = Solution()
array = [11,12,13,14,15,16,17,18,19,20,21,22,23,44,55,66,77,88,1,2,3,4,5,6,7,8,9,10]
res = s.minNumberInRotateArray(array)

# 注意非减数列


