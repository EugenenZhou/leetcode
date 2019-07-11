# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
######################################################################
def lengthofLongSubstring(s):
    num = 0
    length = 0
    char = ''
    for l in s:
        if l not in char:
            char = char + l
            length = length + 1
            if length > num:
                num = length
        else:
            if length > num:
                num = length
            p = char.find(l)
            char = char[p + 1::]
            char = char + l
            length = length - p
    return num
######################################################################
s='abcabcdabd'
result = lengthofLongSubstring(s)
print(s)
