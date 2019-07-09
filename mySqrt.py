
######################################################################
def mySqrt(num):
    #1+3+5+7+9法
    # setnum = 1
    # re = 0
    # while num > 0:
    #     num =num - setnum
    #     setnum = setnum + 2
    #     re = re + 1 if num >= 0 else re
    # return re
    #牛顿迭代
    if num <= 1:
        return num
    r = num
    while r > num / r:
        r = (r + num / r) // 2
    return int(r)

######################################################################
number = 16
result = mySqrt(number)