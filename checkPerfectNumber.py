# 对于一个正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
# 给定一个正整数n，如果他是完美数，返回 True，否则返回 False

######################################################################
def checkPerfectNumber(num):
    if num == 1:
        return False
    s = 1
    #求因子
    i = 2
    j = num
    while i < j:
        if num % i == 0:
            s = s + i + num / i
        j = num // i
        i = i + 1
    if i == j and num % i ==0:
        s = s + i
    return True if s == num else False

######################################################################
number = -5
result = checkPerfectNumber(number)