# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。


######################################################################
def NumberOf1(n):
    if n == -2147483648:
        return 1
    res = 0
    flag = 0
    setting = 0
    union = 31
    if n < 0:
        res = res + 1
        n = -n
        flag = 1
    while n > 0:
            if flag == 0:
                res = res + 1 if n % 2 == 1 else res
            else:
                if setting == 0:
                    if n % 2 == 1:
                        setting = 1
                        res = res + 1
                else:
                    res = res if n % 2 == 1 else res + 1
            n = n // 2
            union = union - 1
    if flag == 0:
        return res
    else:
        return res + union

######################################################################
result = NumberOf1(-2147483648)
print(result)


