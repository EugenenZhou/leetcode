# 求解一个给定的方程，将x以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量 x 和其对应系数。
#
# 如果方程没有解，请返回“No solution”。
#
# 如果方程有无限解，则返回“Infinite solutions”。
#
# 如果方程中只有一个解，要保证返回值 x 是一个整数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/solve-the-equation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
######################################################################
def solveEquation(equation):
    xvalue = 0
    value = 0
    set = 1
    fset = 1
    temp = 0
    forx = 0
    for s in equation:
        if s == 'x':
            if temp != 0:
                xvalue = xvalue + temp
                temp = 0
            elif forx == 1:
                xvalue = xvalue + 0
            else:
                xvalue = xvalue + fset * set * 1
            forx = 0
        elif '0' <= s <= '9':
            temp = 10 * temp + set * fset * int(s)
            forx = 1
        else:
            forx = 0
            if temp != 0:
                value = value + temp
                temp = 0
            if s == '+':
                fset = 1
            elif s == '-':
                fset = -1
            else:
                set = -1
                fset = 1
    if temp != 0:
        value = value + temp
    if xvalue == 0:
        if value == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return 'x=' + str(-value // xvalue)

######################################################################
function = 'x+5-3+x=6+x-2'
result = solveEquation(function)


