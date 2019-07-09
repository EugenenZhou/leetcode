######################################################################
def isPerfectSquare(num):
    #折半查找
    # if num == 0 or num == 1 or num ==4:
    #     return True
    # j = num // 2
    # if num > j * j:
    #     return False
    # i = 0
    # while i < j - 1:
    #     x = (i + j) // 2
    #     if num == x * x:
    #         return True
    #     else:
    #         if num > x*x:
    #             i = x
    #         else:
    #             j = x
    # return False
    ## 1+3+5+7+9法
    setnum = 1
    while num > 0:
        num = num -setnum
        setnum = setnum + 2
    return True if num == 0 else False





######################################################################
number=0
result = isPerfectSquare(number)