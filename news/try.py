import requests
import pymysql
import urllib
from lxml import html
import time
import base64
start = time.time()
url_start = "http://tfs.mof.gov.cn/zhengcejiedu/202103/t20210318_3672512.htm"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
}
params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
response = requests.get(url=url_start, params=params, headers=headers)
response.encoding = "utf-8"
pages_text = response.text
etree = html.etree
tree = etree.HTML(pages_text)
td_xpath = tree.xpath('/html/body/div[5]/div/h2/p[1]')
print(td_xpath)