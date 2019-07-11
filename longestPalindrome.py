# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
######################################################################
def longestPalindrome(s):
    # 中心扩展
    # 添加分隔符
    if not s:
        return s
    news = '#'+ '#'.join(s)+'#'
    # 寻找回文
    length = len(news)
    num = 1
    for mid in range(len(news)):
        temp = 1
        pre = mid - 1
        nex = mid + 1
        while pre >= 0 and nex < length:
            if news[pre] == news[nex]:
                temp = temp + 2
                pre = pre - 1
                nex = nex + 1
            else:
                break
        if temp > num:
            num = temp
            key_pre = pre
            kre_nex = nex
    if num == 3:
        return s[0]
    res = news[key_pre+1:kre_nex]
    return ''.join(res.split('#'))

    # if not s: return s
    # s = '#' + '#'.join(s) + '#'
    # size = len(s)
    # p = [0] * size
    # p[0] = 1
    # mx = 1
    # idx = 0
    # for i in range(size):
    #     if mx > i:
    #         p[i] = min(p[2 * idx - i], mx - i)
    #     else:
    #         p[i] = 1
    #     while i + p[i] <= size - 1 and i - p[i] >= 0:
    #         if s[i + p[i]] == s[i - p[i]]:
    #             p[i] += 1
    #         else:
    #             break
    #     if mx < i + p[i]:
    #         mx = i + p[i]
    #         idx = i
    # target = max(p)
    # pos = p.index(target)
    # res = s[pos - target + 1:pos + target]
    # return ''.join(res.split('#'))

######################################################################
s = ''
result = longestPalindrome(s)