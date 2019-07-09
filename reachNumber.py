# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
# 每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
# 返回到达终点需要的最小移动次数。

######################################################################
def reachNumber(target):
    target = abs(target)
    sum = 0
    i = 1
    while(sum < target):
        sum = sum + i
        i = i + 1
    if (sum - target) % 2 == 0:
        return i-1
    else:
        sum = sum + i
        if (sum-target) % 2 == 0:
            return i
        else:
            return i + 1

######################################################################
target = 11
result = reachNumber(target)