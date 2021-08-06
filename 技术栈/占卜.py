import requests
import pymysql
import urllib
from lxml import html
import time
import re
import base64
start = time.time()
url_start = "https://weread.qq.com/web/reader/2f7329f0718444132f71170kc81322c012c81e728d9d180"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
response = requests.get(url=url_start, params=params, headers=headers)
response.encoding = "utf-8"
pages_text = response.text
# etree = html.etree
# tree = etree.HTML(pages_text)

print(pages_text)