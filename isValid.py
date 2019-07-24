# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def isValid(s):
    # 用栈
    # stack = []
    # for i in s:
    #     if i=='(' or i=='{' or i=='[':
    #         stack.append(i)
    #     elif len(stack) == 0:
    #         return False
    #     elif i == ')' and stack[-1] == "(":
    #         stack.pop()
    #     elif i == '}' and stack[-1] == "{":
    #         stack.pop()
    #     elif i == ']' and stack[-1] == "[":
    #         stack.pop()
    #     else:
    #         return False
    # if len(stack) == 0:
    #     return True
    # else:
    #     return False
    # 高级思维
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('{}','')
        s = s.replace('[]','')
        s = s.replace('()','')
    return False if s else True

######################################################################
ss = "([{]}){()}"
result = isValid(ss)
print(result)