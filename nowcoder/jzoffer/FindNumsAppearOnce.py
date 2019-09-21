# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        res_set = {}
        res = []
        for i in array:
            if i not in res_set:
                res_set[i] = 1
            else:
                res_set[i] += 1
        for i in res_set:
            if res_set[i] == 1:
                res.append(i)
        return res
        # write code here

if __name__ == '__main__':
    s = Solution()
    r = s.FindNumsAppearOnce([4,5,3,2,4,3,7,9,10,21,2,21,9,7,8,5])
    print(r)
    s=[]
    s.insert()