# 登录豆瓣的页面，使用chrome浏览器抓接口
# # 获取豆瓣电影的第一页的数据 并且保存起来

import urllib.request

url = "https://www.zhihu.com/api/v4/me?include=is_realname%2Cad_type%2Cavailable_message_types%2Cdefault_notifications_count%2Cfollow_notifications_count%2Cvote_thank_notifications_count%2Cmessages_count%2Cemail%2Caccount_status%2Cis_bind_phone%2Curl_token%2Cis_destroy_waiting"
# 请求头
headers = {
    "Cookie": "_zap=f7b3a45a-de91-48f5-bae5-47375c8e6457; d_c0=ALDTqU7sRhePThu3hrZ8EWZrji80UqcAt20=|1692676558; __snaker__id=sUOCGPLyZjCjUkFW; YD00517437729195%3AWM_NI=jjw99L0Ypxdngf9Kqi20N5q4anbSMeMIDA%2BEPrpawIXZlhmSbAntwr3ox8Ko3jgIjLLqZVsN%2BRVnsfIwfXrwmkfyWDMcy2PbLGaiuhjDq3JtKOvxdRwrPftO%2ByQTAFRkekU%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea2c249fc999ba5d27da6868aa7d85f939e9b86c166979184acc5638f8d9cd0b62af0fea7c3b92aaab6b9dabc48f487c099e766a5baf7acf463f2f082d6f440a3b2aeb4d06f8f978ca2aa4f94aec082f6439c86a489f059a29fa295f67af1b1b8d9ca65f1b6a9aae94890af96b7f246e98e9a8ff26e8ba9aab9f17dafb5aa9ad6508fbdb7d3d36a9099af8af864aa9cbfd4c9808991ba99e75ab5aea087f745e9a79fb5c44e92b5ab8cd837e2a3; YD00517437729195%3AWM_TID=ijExMzKlJh9FVRBVUBfEzRbbbAnJCG67; q_c1=f46e7a6db9c748e98cb38a0a49953db8|1692676580000|1692676580000; z_c0=2|1:0|10:1698219040|4:z_c0|80:MS4xdkVmeUR3QUFBQUFtQUFBQVlBSlZUZVR0STJiZjJYSHNBTW9Wb2x2Y3U2X0xCSnBGZENsVDNRPT0=|5d892ee2406c27df755abda09f068bc7957a051f771b453f2a8f7eea9ac04839; _xsrf=67589400-cd50-4d30-8638-4f79150d3926; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1698660290,1698738093,1698807185,1698982410; tst=r; SESSIONID=h7dOozFVA25P6vepp9tui8UzGSS1N8t7f4c9MRkal3X; JOID=W1gXB0L5Q4_LozJIFvWq1Ybn0wcKmHbticxBDEa4eLidmEQkZCbHwKOqOUwddjiMHK_s0wK5lScfJLQ1zxL1zKw=; osd=W10QBkn5RojKqDJNEfSh1YPg0gwKnXHsgsxEC0ezeL2amU8kYSHGy6OvPk0Wdj2LHaTs1gW4nicaI7U-zxfyzac=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1698988252; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1698988267|1698988241"
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 获取响应数据
response = urllib.request.urlopen(request)

# 获取响应数据,是字符串格式
content = response.read().decode("utf-8")

file = open("movie.json", "w", encoding="utf-8")
file.write(content)
print(content)
