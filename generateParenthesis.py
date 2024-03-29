# 给出 n 代表生成括号的对数，请你写出一个函数，
# 使其能够生成所有可能的并且有效的括号组合。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def generateParenthesis(n):
    if n == 0:
        return []
    pre = {'()'}
    for i in range(n - 1):
        now = set()
        for st in pre:
            n = len(st)
            for index in range(n):
                now.add(st[0:index] + '()' + st[index:n])
        pre = now
    return list(pre)
######################################################################
number = 3
result = generateParenthesis(number)
print(result)
