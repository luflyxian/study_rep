import requests
from lxml import html
from urllib.parse import urljoin
import time
import re
import execjs
import urllib
import base64

start = time.time()
url_start = "http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index2.html" #当前总共有292页数据，从page=1开始
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
etree = html.etree
tree = etree.HTML(pages_text)
xd_url=tree.xpath('//*[@id="11040"]/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/font/a/@href')#table
shijian=tree.xpath('//*[@id="11040"]/div[2]/div[1]/table/tbody/tr[2]/td/table[1]/tbody/tr/td[2]/span/text()')
print(f"一共花费{time.time() - start}")
for i in xd_url:
    url_one = "http://www.pbc.gov.cn/"
    url = urllib.parse.urljoin(url_one, i)
    sess = requests.session()
    jsPage = sess.get(url).text
    js = re.findall(r'<script type="text/javascript">([\w\W]*)</script>', jsPage)[0]
    js = re.sub(r'atob\(', 'window["atob"](', js)
    js2 = 'function getURL(){ var window = {};' + js + 'return window["location"];}'
    ctx = execjs.compile(js2)
    tail = ctx.call('getURL')
    URL2 = urljoin(url, tail)
    page = sess.get(URL2)
    page.encoding = 'UTF-8'
    pages_text = page.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    keys = base64.b64encode(url.encode("utf8"))
    key = str(keys, encoding="utf8")
    zhuti = tree.xpath('//*[@id="10929"]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/h2/text()')
    sj1= tree.xpath('//*[@id="10929"]/div[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td[4]/text()')
    fabushijian = [x.strip() for x in sj1 if x.strip() != '']
    time.sleep(0.5)
    neirong1 = tree.xpath('//*[@id="zoom"]/p//text()')
    nr = []
    for x in neirong1:
        nr.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
    neirong1 = [x.strip() for x in nr if x.strip() != '']
    neirong = [neirong5 + "\n" for neirong5 in neirong1]
    wzbsm = '网站标识码：bm25000001'
    ipbeianhao = '京ICP备05073439号'
    beianhao = '京公网安备 11010202000016号'
    print(key)
    print(zhuti)
    print(fabushijian)
    print(neirong)
    print(wzbsm)
    print(ipbeianhao)
    print(beianhao)