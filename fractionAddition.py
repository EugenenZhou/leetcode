# 给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。 
# 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，
# 例如 2，你需要将它转换成分数形式，其分母为 1。
# 所以在上述例子中, 2 应该被转换为 2/1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fraction-addition-and-subtraction
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def fractionAddition(expression):
    top_value = 0
    bottom_value = 0
    top_temp = 0
    bottom_temp = 0
    flag = 0
    set = 1

    def gcd(a, b):
        # 最大公约
        return b if a % b == 0 else gcd(b, a % b)

    def lcm(a, b):
        # 最小公倍
        return int(a * b // gcd(a, b))

    for s in expression:
        if '0' <= s <= '9':
            if flag == 0:
                top_temp = 10 * top_temp + set * int(s)
            else:
                bottom_temp = 10 * bottom_temp + int(s)
        elif s == '+' or s == '-':
            if s == '-':
                set = -1
            if flag == 1:
                if top_value == 0 or bottom_value == 0:
                    top_value = top_temp
                    bottom_value = bottom_temp
                    top_temp = 0
                    bottom_temp = 0
                    flag = 0
                else:
                    lcm_value = lcm(bottom_value, bottom_temp)
                    top_value = lcm_value / bottom_value * top_value + lcm_value / bottom_temp * top_temp
                    bottom_value = lcm_value
                    top_temp = 0
                    bottom_temp = 0
                    flag = 0
        elif s == '/':
            set = 1
            flag = 1

    if top_value == 0 or bottom_value == 0:
        top_value = top_temp
        bottom_value = bottom_temp
    else:
        lcm_value = lcm(bottom_value, bottom_temp)
        top_value = lcm_value / bottom_value * top_value + lcm_value / bottom_temp * top_temp
        bottom_value = lcm_value
    gcd_value = gcd(top_value, bottom_value)
    top_value = top_value / gcd_value
    bottom_value = bottom_value / gcd_value
    return str(int(top_value))+'/'+str(int(bottom_value))


######################################################################
exp="-1/2+1/2"
result = fractionAddition(exp)
