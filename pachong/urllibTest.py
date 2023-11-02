# -*- coding: utf-8 -*-

# 使用urllib获取
import urllib.request
import urllib.parse

# 定义一个url，也就是要访问的对地址
url = "https://www.baidu.com/s?wd="


# 模拟浏览器向服务器发送请求
# response的数据类型是HTTPResponse
# response = urllib.request.urlopen(url)

# # 获取响应中的页面的源码,read方法返回的是字节数据
# # 将二进制数据转换为字符串数据，二进制-》字符串称为解码，
# # response.read(5)一个字节一个字节的读，返回5个字节
# content = response.read(5).decode("utf-8")

# # 只读取一行
# content = response.readline()


# # 读取所有行
# content = response.readlines()

# # 返回状态码，如果是200，那么证明逻辑没错
# content = response.getcode()

# # 返回url地址
# content = response.geturl()

# # 获取状态信息，
# content = response.getheaders()

# # 打印数据
# print(content)


# 下载图片/网页/视频/音频等
# 参数url，是下载路径，也就是连接地址
# filename是文件的名字
urllib.request.urlretrieve(url, "wannianli.html")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}


url = "https://www.baidu.com/s?wd="
# 由于urlopen方法中不能使用字典，所以不能将上述headers直接传入urllib.request.urlopen(url,headers)
# 请求对象的定制,为了解决反爬的第一种手段
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)

# 使用urllib获取
import urllib.request
import urllib.parse

# 如果，url中存在中文字符，那么上面的方式就会报错，可以使用urllib.parse将中文字符转化成unicode编码
name = urllib.parse.quote("周杰伦")  # 将汉字编码成unicode编码
url = url + name
print(url)
