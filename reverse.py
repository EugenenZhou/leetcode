# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
######################################################################
def reverse(x):
    intmax = 2**31 - 1
    set = 1
    if x < 0:
        intmax = intmax + 1
        x = -x
        set = -1
    number = 0
    while x != 0:
        temp = x % 10
        x = x // 10
        if number * 10 + temp > intmax:
            return 0
        number = number * 10 + temp
    return set * number
######################################################################
num = -123
result =reverse(num)
print(result)
