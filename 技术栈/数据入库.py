import requests
from lxml import html
import time
import pymysql
import base64

def get_first_url(url,params,headers):
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    zhuti1 = tree.xpath('//div[@class="article oneColumn pub_border"]/h1/text()')#标题
    shijian1 = tree.xpath('//div[@class="pages-date"]/text()')#时间
    neirong=tree.xpath("//p[@style='text-indent: 2em; font-family: 宋体; font-size: 12pt;']/text()")#内容
    zhuti = [x.strip() for x in zhuti1 if x.strip() != '']
    shijian = [x.strip() for x in shijian1 if x.strip() != '']
    key1 = base64.b64encode(url.encode("utf8"))
    key = str(key1, encoding="utf8")

    # print(key)
    # print(zhuti)
    # print(shijian)
    # print(neirong)
    connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456", db="XCX",
                              charset='utf8')
    cursor = connect.cursor()
    sql = 'INSERT ignore INTO xcx_body(`keys`,`zt`,`sj`,`nr`)VALUES("' + str(key) + '","' + str(zhuti) + '","' + str(shijian) + '","' + str(neirong) + '")'
    cursor.execute(sql)
    connect.commit()
    connect.close()
    # sql = "truncate xcx_body"
    # cursor.execute(sql)
    print(f"一共花费{time.time() - start}")

if __name__ == "__main__":
    start = time.time()

    url = "http://www.gov.cn/xinwen/2021-02/27/content_5589166.htm"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    get_first_url(url,params,headers)









    # texts = str(shijian)
    # a = texts.replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
    # b = a.replace("['", '').replace("']", '')
    # c = ' 12:00:00';
    # shijian = b + c