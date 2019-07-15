# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
######################################################################
def convert(s, numRows):
    # if numRows <= 1:
    #     return s
    # num = 0
    # st = []
    # result=''
    # set = -1
    # p = numRows - 2
    # while num < len(s):
    #     if num < numRows:
    #         st.append(str(s[num]))
    #         num = num + 1
    #         continue
    #     st[p] = st[p]+ str(s[num])
    #     if p == 0:
    #         set = 1
    #     elif p == numRows-1:
    #         set = -1
    #     p = p + set
    #     num = num + 1
    # for i in st:
    #     result = result + i
    # return result
##
    if numRows == 1:
        return s
    s_rows = [""] * numRows
    s_len = len(s)
    loop_len = 2 * numRows - 2
    for i in range(s_len):
        ref_num = i % loop_len
        if ref_num >= numRows:
            ref_num = 2 * numRows - ref_num - 2
        s_rows[ref_num] += s[i]
    return "".join(s_rows)

######################################################################
s = "LEETCODEISHIRING"
numrow = 3
result = convert(s,numrow)
print(result)

