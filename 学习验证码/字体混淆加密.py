import requests
from lxml import html
import time
import pymysql
import base64
import urllib

start = time.time()
url_start = "https://www.dianping.com/nanchang/ch10"
headers = {
"Cookie":"cy=134; cye=nanchang; _lxsdk_cuid=17aa98c8192c8-0cd47bee2fed6-6373264-240000-17aa98c8193c8; _lxsdk=17aa98c8192c8-0cd47bee2fed6-6373264-240000-17aa98c8193c8; _hc.v=1cefdd00-7af9-2932-f1e1-1bf761139085.1626342196; s_ViewType=10; fspop=test; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic%26utm_term%3D%25E5%25A4%25A7%25E4%25BC%2597%25E7%2582%25B9%25E8%25AF%2584; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1626342196,1627348559,1627441578,1627444754; _lxsdk_s=17aec4b5913-49a-90b-72d%7C%7C21; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1627462500"
,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
,"Host":"www.dianping.com"
    ,"Referrer Policy":"strict-origin-when-cross-origin"
}

# response.encoding = "utf-8"
# pages_text = response.text

new_map = {
    '0xee82': '1',
    '0xe2c5': '2',
    '0xe32e': '3',
    '0xeff7': '4',
    '0xf5a0': '5',
    '0xe463': '6',
    '0xea1c': '7',
    '0xed5a': '8',
    '0xebca': '9',
    '0xeac6': '0'
}

rs = {}
for k, v in new_map.items():
    rs['&#' + k[1:] + ';'] = v

res = requests.get(url=url_start, headers=headers).text

for k,v in rs.items():
    if k in res:
        res = res.replace(k,v)
# print(res)

pages_text = res
etree = html.etree
tree = etree.HTML(pages_text)
td_xpath = tree.xpath('//*[@id="shop-all-list"]/ul/li[1]/div[2]/div[2]/a[2]/b//text()')
# td_xpath2 = tree.xpath('//*[@id="shop-all-list"]/ul/li[1]/div[2]/div[2]/a[2]/b/svgmtsi[2]/text()')
# td_xpath = td_xpath1 +td_xpath2

a = ''.join(td_xpath)
print(a)