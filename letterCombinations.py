# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
######################################################################
def letterCombinations(digits):
    dic ={'2':['a','b','c'],
          '3':['d','e','f'],
          '4':['g','h','i'],
          '5':['j','k','l'],
          '6':['m','n','o'],
          '7':['p','q','r','s'],
          '8':['t','u','v'],
          '9':['w','x','y','z'],
          }
    res = []
    def backtrack(comb,next):
        if len(next) == 0:
            res.append(comb)
        else:
            for letter in dic[next[0]]:
                backtrack(comb+letter,next[1:])
    if digits:
        backtrack('',digits)
    return res

######################################################################
dig = '23'
result = letterCombinations(dig)
print(result)