# 矩形覆盖

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# 斐波那契数列

######################################################################
def rectCover(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    a = 1
    b = 2
    number = number - 2
    while number > 0:
        b = a + b
        a = b - a
        number = number -1
    return b

######################################################################
n = 5
res = rectCover(n)
print(res)