# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        if not s:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if not s:
            return False
        length = len(s)
        flag_e = 0
        flag_p = 0
        for i in range(length):
            if s[i] >= '0' and s[i] <= '9':
                pass
            elif s[i] == 'e' or s[i] == 'E':
                if flag_e:
                    return False
                flag_e = 1
                if i == length - 1:
                    return False
            elif s[i] =='.':
                if flag_p or flag_e:
                    return False
                flag_p = 1
                if i == length - 1:
                    return False
                if s[i+1] < '0' or s[i+1] > '9':
                    return False
            elif s[i] =='+' or s[i] =='-':
                if i == length - 1:
                    return False
                if s[i+1] < '0' or s[i+1] > '9':
                    return False
                if s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            else:
                return False
        return True
        # write code here

if __name__ == '__main__':
    s = Solution()
    r = s.isNumeric('123.45e+6')
    print(r)