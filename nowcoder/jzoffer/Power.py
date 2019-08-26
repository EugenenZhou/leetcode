# 数值的整数次方

# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#
# 保证base和exponent不同时为0
######################################################################
class Solution:
    def Power(self, base, exponent):
        if exponent < 0:
            exponent = exponent * -1
            base = 1 / base
        if exponent == 0:
            return 1
        half = self.Power(base, exponent // 2)
        if exponent % 2 == 0:
            return half * half
        else:
            return half * half * base

######################################################################