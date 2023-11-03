# （1） 请求对象的定制
# （2） 获取响应的数据
# （3） 下载数据

import urllib.parse
import urllib.request


def create_request(page):
    base_url = (
        "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"
    )

    data = {"start": (page - 1) * 20, "limit": 20}
    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    with open("douban_" + str(page) + ".json", "w", encoding="utf-8") as fp:
        fp.write(content)


# 程序的入口
if __name__ == "__main__":
    start_page = int(input("请输入起始的页码"))
    end_page = int(input("请输入结束的页面"))

    for page in range(start_page, end_page + 1):
        #         每一页都有自己的请求对象的定制
        request = create_request(page)
        #         获取响应的数据
        content = get_content(request)
        #         下载
        down_load(page, content)


import urllib.request

url = "http://www.baidu.com"

headers = {
    "User ‐ Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML,likeGecko) Chrome / 74.0.3729.169Safari / 537.36"
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# handler build_handler open


# 1.获取handler对象
handler = urllib.request.HTTPHandler()
# 2.通过handler获取opener对象
opener = urllib.request.build_opener(handler)
# 3.调用open方法
response = opener.open(request)

print(response.read().decode("utf‐8"))


import urllib.request

url = "http://www.baidu.com/s?wd=ip"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies = {"http": "IP:Port"}
# handler  build_opener  open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode("utf-8")

# 保存
with open("daili.html", "w", encoding="utf-8") as fp:
    fp.write(content)


proxies_pool = [{"http": "118.24.219.151:16817"}, {"http": "118.24.219.151:16817"}]

import random

proxies = random.choice(proxies_pool)
