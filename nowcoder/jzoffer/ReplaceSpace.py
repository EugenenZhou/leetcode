# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.
# 则经过替换之后的字符串为We%20Are%20Happy。


# 提示：从后往前移动
######################################################################
class Solution():
    def ReplaceSpace(self ,s):
        if ' ' not in s:
            return s
        sb = '#'+ s
        string = ''
        top = 0
        for index,st in enumerate(sb):
            if st == ' ':
                string = string + sb[top:index]+'%20'
                top = index + 1

        return string[1::] + sb[top::]

######################################################################

s = 'helloworld'
result = Solution()
re = result.ReplaceSpace(s)