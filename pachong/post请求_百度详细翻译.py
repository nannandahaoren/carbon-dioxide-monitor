import urllib.request
import urllib.parse
import json

# 请求对象，连接地址
url = "https://fanyi.baidu.com/sug"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
# 请求数据
data = {"kw": "spider"}
# post请求的参数，必须要进行编码,还要调用encode方法
data = urllib.parse.urlencode(data).encode("utf-8")

# post请求阐述不会拼接在url后面，而是以data参数的形式给出
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据,是字符串格式
content = response.read().decode("utf-8")

# 获取响应数据
obj = json.loads(content)
print(obj)
