# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
######################################################################
def isMatch(s,p):
    if not p: return not s
    first_match = bool(s) and p[0] in {s[0],'.'}
    if len(p) >= 2 and p[1] == '*':
        return isMatch(s,p[2:]) or first_match and isMatch(s[1:],p)
    else:
        return first_match and isMatch(s[1:],p[1:])
######################################################################
'''
#字符串比较
def isMatch(s,p):
    if len(s)!=len(p):
        return False
    for i in range(len(s)):
        if s[i] != p[i]:
            return False
    return True

#改进
def isMatch(s,p):
    i = 0
    j = 0
    while (j < len(p)):
        if (i >= len(s)):
            return False
        if p[j] != s[i]:
            return False
        else:
            j=j+1
            i=i+1
    return j == len(s)


# 引入递归思想
def isMatch(s, p):
    if not p: return not s
    first_match = s and p[0] == s[0]
    return first_match and isMatch(s[1:], p[1:])

# 加上通配符 [.]
def isMatch(text, pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and isMatch(text[1:], pattern[1:])

# 加上通配符 [*]
def isMatch(text,pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0],'.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        return isMatch(text,pattern[2:]) or first_match and isMatch(text[1:],pattern)
    else:
        return first_match and isMatch(text[1:],pattern[1:])
'''
######################################################################
text = "aa"
pattern = "a"
result = isMatch(text,pattern)
print(result)