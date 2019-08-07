# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def findSubstring(s,words):
    # if not s or not words:
    #     return []
    # Hash1={}
    # word_number = len(words)
    # word_length = len(words[0])
    # res = []
    # for i in range(word_number):
    #     if words[i] in Hash1:
    #         Hash1[words[i]] += 1
    #     else:
    #         Hash1[words[i]] = 1
    # for length in range(len(s)-word_number*word_length+1):
    #     j = 0
    #     Hash2 = {}
    #     while j < word_number:
    #         temp_word = s[j*word_length+length:j*word_length+length+word_length]
    #         if temp_word in Hash1:
    #             if temp_word in Hash2:
    #                 Hash2[temp_word] += 1
    #                 if Hash2[temp_word] > Hash1[temp_word]:
    #                     break
    #             else:
    #                 Hash2[temp_word] = 1
    #         else:
    #             break
    #         j=j+1
    #     if Hash2 == Hash1:
    #         res.append(length)
    # return res


    if s == "" or len(s) == 0 or words == [] or len(words) == 0 or len(words[0]) == 0 or len(s) < len(words) * len(
            words[0]):
        return []

    lens = len(s)
    lenw = len(words[0])
    lenws = lenw * len(words)
    counter = {}
    for i in words:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    result = []
    # 如果lenw=4,lens-lenws+1=3,那么至多三种间隔情况
    # 而如果lenw<lens-lenws+1，那么用lenw是可以遍历所有情况的
    for i in range(min(lenw, lens - lenws + 1)):
        s_pos = i
        word_pos = i
        d = {}
        while s_pos + lenws <= lens:
            word = s[word_pos:word_pos + lenw]
            word_pos += lenw
            if word not in counter:
                s_pos = word_pos
                d.clear()
            else:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
                while d[word] > counter[word]:  # 如果现在word的数量大于counter中的数量，意味着前面保存的要全部删除。
                    # 这里要从起点开始消除，直到找到重复点在哪为止
                    d[s[s_pos:s_pos + lenw]] -= 1
                    s_pos += lenw

                if word_pos - s_pos == lenws:
                    result.append(s_pos)
    return result



######################################################################
s="wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
# s = "barfoothefoobarman"
# words = ["foo","bar"]
result = findSubstring(s,words)
print(result)

