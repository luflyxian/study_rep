import requests
from lxml import html
import time
import re

def get_first_url(url,params,headers):
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    shijian = tree.xpath('//table[@style="width:660px;margin:0 auto;margin-top:12px;"]/tbody/tr[4]/td[4]/text()')#时间
    #print(shijian)
    print(f"一共花费{time.time() - start}")
    texts = str(shijian)
    a = texts.replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
    b = a.replace("['", '').replace("']", '')
    c = ' 12:00:00' ;d=b+c
    print(d)
    timeArray = time.strptime(d, "%Y-%m-%d %H:%M:%S")
   # print(timeArray)
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)#-----------------------------时间戳

if __name__ == "__main__":
    start = time.time()
    #url = "http://www.gov.cn/zhengce/2021-02/23/content_5588496.htm"
    #url = "http://www.gov.cn/zhengce/content/2021-02/19/content_5587668.htm"
    url="http://www.gov.cn/zhengce/content/2021-02/09/content_5586306.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    get_first_url(url,params,headers)
