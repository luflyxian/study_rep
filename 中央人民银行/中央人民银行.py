import requests
from lxml import html
from urllib.parse import urljoin
import time
import re
import execjs
import urllib

start = time.time()
for i in range(1,6):
    url_start = "http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index"+str(i)+".html"  # 当前总共有292页数据，从page=1开始
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    sess = requests.session()
    jsPage = sess.get(url_start).text
    js = re.findall(r'<script type="text/javascript">([\w\W]*)</script>', jsPage)[0]
    js = re.sub(r'atob\(', 'window["atob"](', js)
    js2 = 'function getURL(){ var window = {};' + js + 'return window["location"];}'
    ctx = execjs.compile(js2)
    tail = ctx.call('getURL')
    URL2 = urljoin(url_start, tail)
    page = sess.get(URL2)
    page.encoding = 'UTF-8'
    pages_text = page.text
    print(pages_text)
    etree = html.etree
    tree = etree.HTML(pages_text)



print(f"一共花费{time.time() - start}")
