import requests
import re
from urllib.parse import urljoin
import execjs

url = 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index1.html'


# res=requests.get(url)
# res.encoding='utf-8'
# print(res.text)

def getPage(URL):
    sess = requests.session()
    jsPage = sess.get(URL).text
    js = re.findall(r'<script type="text/javascript">([\w\W]*)</script>', jsPage)[0]
    js = re.sub(r'atob\(', 'window["atob"](', js)

    js2 = 'function getURL(){ var window = {};' + js + 'return window["location"];}'

    ctx = execjs.compile(js2)
    #print(ctx)
    tail = ctx.call('getURL')
    #print(tail)
    URL2 = urljoin(URL, tail)
    print(URL2)
    page = sess.get(URL2)
    page.encoding = 'UTF-8'
    print(page)


print(getPage(url))
