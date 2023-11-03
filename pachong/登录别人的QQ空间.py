# 适用的场景：数据采集的时候 需要绕过登陆 然后进入到某个页

# 个人信息页面是utf-8 但是还报错了编码错误 因为并没有进入到个人信息页面 而是跳转到了登陆页面 那么登陆页面不是utf-8 所以报错

# 什么情况下访问不成功 ?
# 因为请求头的信息不够 所以访问不成功
import urllib.request

url = "https://weibo.cn/6451491586/info"

headers = {
    "accept-language": "zh-CN,zh;q=0.9",
    # cookie中携带着你的登陆信息   如果有登陆之后的cookie  那么我们就可以携带着cookie进入到任何页面
    "cookie": "xxxxxx",
    # referer  判断当前路径是不是由上一个路径进来的    一般情况下 是做图片防盗链
    "referer": "https://weibo.cn/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode("utf-8")

# 将数据保存到本地
with open("weibo.html", "w", encoding="utf-8") as fp:
    fp.write(content)
