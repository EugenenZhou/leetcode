# 一个黑板上写着一个非负整数数组 nums[i] 。
# 小红和小明轮流从黑板上擦掉一个数字，小红先手。
# 如果擦除一个数字后，剩余的所有数字按位异或运算得出的结果等于 0 的话，当前玩家游戏失败。 
# (另外，如果只剩一个数字，按位异或运算得到它本身；如果无数字剩余，按位异或运算结果为0。）
# 换种说法就是，轮到某个玩家时，如果当前黑板上所有数字按位异或运算结果等于 0，这个玩家获胜。
# 假设两个玩家每步都使用最优解，当且仅当小红获胜时返回 true。
######################################################################

def xorGame(nums):
    re = 0
    for i in nums:
        re = re ^ i
    if re == 0:
        return True
    else:
        if len(nums) % 2 == 0:
            return True
        else:
            return False
    pass

######################################################################
# 小红必胜的可能性为，先手异或为0，或nums中的元素为偶数，其他才有可能小明胜利。
nums = [1,1,2,3]
result = xorGame(nums)
