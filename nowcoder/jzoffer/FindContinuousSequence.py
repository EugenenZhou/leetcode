# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1)>>1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big+1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output
        # num = 2
        # res = []
        # while tsum / num - (num // 2) > 0:
        #     if num % 2 == 0:
        #         if tsum / num - 0.5 == tsum // num:
        #             s = tsum // num
        #             res.insert(0,range(s - (num-1)//2,s + num//2+1))
        #     else:
        #         if tsum / num == tsum // num:
        #             s = tsum // num
        #             res.insert(0,range(s - num//2, s + num // 2+1))
        #     num = num + 1
        # return res
        # write code here


if __name__ == '__main__':
    s = Solution()
    r = s.FindContinuousSequence(3)
    print(r)
