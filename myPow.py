# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
######################################################################
def myPow(x,n):
    if n < 0:
        n = n * -1
        x = 1 / x
    if n == 0:
        return 1
    half = myPow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             n = n * -1
#             x = 1/x
#         if n == 0:
#             return 1
#         half = self.myPow(x, n // 2)
#         if n % 2 == 0:
#             return half * half
#         else:
#             return half * half * x
######################################################################
# 对半 除2余0 对半乘 除2余1 对半乘再乘x
######################################################################
num=2.00000
n=12
result = myPow(num,n)
# result = Solution().myPow(num,n)