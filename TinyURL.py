# TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
# 它将返回一个简化的URL http://tinyurl.com/4e9iAk.
#
# 要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。
# 你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，
# 并且这个TinyURL可以用解密方法恢复成原本的URL。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/encode-and-decode-tinyurl
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
######################################################################
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
######################################################################
# url = 'https://leetcode.com/problems/design-tinyurl'
# codec = Codec()
# codec.decode(codec.encode(url))

from urllib.parse import quote, unquote

name = "周1"

# 编码
utf8_name = quote(name)  # utf-8
print(utf8_name)
# %E7%8E%8B%E5%A4%A7%E9%94%A4   长度是 9

gbk_name = quote(name, encoding="gbk")
print(gbk_name)
# %CD%F5%B4%F3%B4%B8    长度是 6

# 解码
print(unquote(utf8_name))
print(unquote(gbk_name, encoding="gbk"))
# 王大锤

