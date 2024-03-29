####################################################################
# 我们可以观察到每 1010 个数，个位上的’1’ 就会出现一次。
# 同样的，每 100100 个数，十位上的’1’ 就会出现一次。
# 这个规律可以用 (n/(i*10))*i(n/(i∗10))∗i 公式来表示。
# 同时，如果十位上的数是 ’1’，那么最后’1’ 的数量要加上 x+1，其中 x 是个位上的数值。
# 如果十位上的数大于’1’，那么十位上为’1’ 的所有的数都是符合要求的，这时候最后’1’ 的数量要加 10。
# 这个规律可以用公式 min(max((n mod (i*10))-i+1,0),i)来表示。
# 我们来看一个例子吧，有一个数 n = 1234。
# 个位上’1’的数量 = 1234/10 (对应 1,11,21,...1221) + min(4,1) (对应 1231) = 124
# 十位上’1’的数量 = (1234/100)*10 (对应 10,11,12,...,110,111,...1919) + min(21,10) (对应 1210,1211,...1219) = 130130
# 百位上’1’的数量 = (1234/1000)*100(对应 100,101,102,...,199) + min(135,100) (对应1100,1101...1199) = 200200
# 千位上’1’的数量 = (1234/10000)*10000(1234/10000)∗10000 + min(235,1000) (对应1000,1001,...1234) = 235235
# 因此，总数 = 124+130+200+235 = 689124+130+200+235=689。
# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/two-sum/solution/shu-zi-1-de-ge-shu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
####################################################################
def countDigitOne(n,method):
    if method == 1:
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        else:
            n = str(n)
            a,b = int(n[0]),int(n[1:])
            if a == 1:
                return 1+b+countDigitOne(b,1)+countDigitOne(10**(len(n)-1)-1,1)
            else:
                return 10**(len(n)-1)+countDigitOne(b,1)+a*countDigitOne(10**(len(n)-1)-1,1)

    elif method == 2:
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        else:
            result = 0
            for i in range(len(str(n))):
                result= result + (n // (10**(i+1)))*(10**i) + min(10**i, n%(10**(i+1))-10**i+1 if n%(10**(i+1))-10**i+1 >=0 else 0)
            return result


num=134
result=countDigitOne(num,method=2)