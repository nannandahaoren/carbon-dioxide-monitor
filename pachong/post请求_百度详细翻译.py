import urllib.request
import urllib.parse
import json

# 请求对象，连接地址
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

# 请求头
# 去掉编码格式
headers = {
    "Cookie": "BIDUPSID=46FDCEEEFDFCEADCA7CCE91C1D3D9F46; PSTM=1692106454; BAIDUID=46FDCEEEFDFCEADC54E56EE23C0BC4FE:FG=1; APPGUIDE_10_6_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_6_5=1; APPGUIDE_10_6_6=1; H_WISE_SIDS=110085_268593_269904_271169_270102_272278_273120_274778_275941_276572_276592_271562_276965_277355_273982_277641_277636_275188_277785_275733_277950_277996_259642_278053_278396_278414_278574_278763_278733_278790_278388_279041_276424_277759_279264_279323_8000056_8000104_8000121_8000142_8000145_8000149_8000162_8000171_8000177_8000179_8000184_8000185; H_WISE_SIDS_BFESS=110085_268593_269904_271169_270102_272278_273120_274778_275941_276572_276592_271562_276965_277355_273982_277641_277636_275188_277785_275733_277950_277996_259642_278053_278396_278414_278574_278763_278733_278790_278388_279041_276424_277759_279264_279323_8000056_8000104_8000121_8000142_8000145_8000149_8000162_8000171_8000177_8000179_8000184_8000185; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-%3A; delPer=0; PSINO=2; BA_HECTOR=2h8ga4a1208lak2h2la58k0k1ik4fce1r; ZFY=NFtZip71NLFSPP8DoK:AGc8pLnLvMS5MfzGQ1l46SN50:C; BAIDUID_BFESS=46FDCEEEFDFCEADC54E56EE23C0BC4FE:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=39396_39530_39418_39590_39437_39527_39521_39497_39467_26350_39560; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1697016685,1698062008,1698719905,1698896882; ab_sr=1.0.1_ZTdmZTdiOWI3MTAyMDhiZWQ3MWUwNGU0ZGFlY2E0YTcxOGM2Y2FiZmY5MjhiODQ4Y2MxMjI3OGQ5YzU0ZTg3YmYyY2I2N2RmMzQzZjJlZGRkYTg5NGY4ODY0MDY0ZGRjMDQzMDcyNzAwY2EzNWQwYWQ5NWJiZTU5NTZmZTNhMzE0NWNiYjdjNWNhN2U3NWU3MGQ4ODdjZWM2OWYxODEwOA==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1698898555",
    "Host": "fanyi.baidu.com",
    "Origin": "https://fanyi.baidu.com",
    "Referer": "https://fanyi.baidu.com/",
    "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Acs-Token": "1698898555459_1698898555425_K5yHdEJLLIKr0lnss5BndOdOrAFFuG/3UuT1Bd1AxW/m5IZlYjji2wppPB7wuCAAdrhfbrws6O9IqYBeiWbr8usqSYlQNTzkwksmKkP4YX2RhvjSUksNHM5Dw6cOhJdZvhv9zQG2PgfBZ8Bcq/z45f5bRuqOmQ26vuQLCOxgyNt0nMpYUjUKbfTgQrURjTyBwJ+Jx5QsA/NSOO2qNX0tB93mlY9oGY3suKVkXvsJLzyejEoG6gGh/38+cqBB1JZHPitJLlqIDelOPkiTU3a06dyB0a5vHwUQWNUfjvmACPLHW4+NpaU+vdwDFam88Bs7Gis3rurMV3d+X5RBDZfpiPy2HRAXTJMLMB1f06KpAZ6guIE2E+6vD8e9yMlez47ytYhkS+uL4+OBlyoh76rOiPPrucBgFH+WHCr0FC02EFrcmLxorhCIb2pnCEtxHOajsD67Zg1cSRHOye/5X/MQyo3WHgm4PAQ+zjwnirmgkE7SsiJSLBABeeQRnw+0T61T",
}

# 请求数据
data = {
    "from": "en",
    "to": "zh",
    "query": "spider",
    "transtype": "enter",
    "simple_means_flag": "3",
    "sign": "63766.268839",
    "token": "10808e209716e469ba9dd2309f81d986",
    "domain": "common",
    "ts": "1698904049462",
}

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
