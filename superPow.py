# 你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
######################################################################
# def superPow(a,b):
#     result = pow(a,int(''.join(map(str,b))),1337)
#     return result
def superPow(a,b):
    a = a % 1337
    result = Fun(a,b,len(b))
    return result

def Fun(a,b,len):
    res = 1
    if len > 1:
        pre = Fun(a,b,len-1)
        for i in range(0,10):
            res = res * int(pre)
            res = res % 1337
    rest = 1
    count = b[len-1]
    for i in range(0,count):
        rest = rest * a
        rest = rest % 1337
    res =res * rest

    res = res % 1337
    return res

######################################################################
a = 2
b = [3,2,0]
result = superPow(a,b)

# int("".join(map(str, b)))