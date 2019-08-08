# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-valid-parentheses/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


######################################################################
def longestValidParentheses(s):
    # 弹出
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
        # dp数组存储    法
        # n = len(s)
        # if n == 0: return 0
        # dp = [0] * n
        # res = 0
        # for i in range(n):
        #     if i > 0 and s[i] == ")":
        #         if s[i - 1] == "(":
        #             dp[i] = dp[i - 2] + 2
        #         elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
        #             dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        #         if dp[i] > res:
        #             res = dp[i]
        # return res
        #左右遍历法
        #暴力法

######################################################################
string = "())()()((()())())()()))((()())"
result = longestValidParentheses(string)
print(result)
