# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
######################################################################
def longestCommonPrefix(strs):
    if not strs or '' in strs: return ''
    temp = strs[0]
    for i in range(1, len(strs)):
        for j in range(len(temp)):
            if temp[j] != strs[i][j] and j == 0:
                return ''
            if temp[j] != strs[i][j]:
                temp = temp[0:j]
                break
            if j == len(strs[i])-1:
                temp = temp[0:j+1]
                break
    return temp
######################################################################
string = ['','','a']
result = longestCommonPrefix(string)
print(result)