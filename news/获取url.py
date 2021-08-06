import requests
import pymysql
import urllib
from lxml import html
import re
import time
count = 0
def get_first_url(url_start, params, headers):
    response = requests.get(url=url_start, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    td_xpath = tree.xpath('//ul[@class="listTxt"]/li/h4/a/@href')
    for i in td_xpath:
        url_one = "http://www.scio.gov.cn/xwfbh/gssxwfbh/xwfbh/jiangxi/"
        url = urllib.parse.urljoin(url_one, i)  # ---------------------------------------url
        print(url)
    print(f"一共花费{time.time() - start}")


if __name__ == "__main__":
    start = time.time()
    url_start = "http://sousuo.gov.cn/column/30469/0.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    get_first_url(url_start, params, headers)

    # neirong = []
    # for x in neirong3:
    #     neirong.append(x+'\n')
    # print(neirong)